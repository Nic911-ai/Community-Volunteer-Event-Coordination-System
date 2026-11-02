import re, datetime
from functools import wraps
import mysql.connector
from flask import Flask, render_template, request, redirect, url_for, session, flash, abort
from werkzeug.security import generate_password_hash, check_password_hash
from config import DB, RULES, SECRET_KEY

app = Flask(__name__); app.secret_key = SECRET_KEY

def q(sql, args=(), one=False, write=False):
    """Run a parameterised query (protects against SQL injection)."""
    c = mysql.connector.connect(**DB); cur = c.cursor(dictionary=True); cur.execute(sql, args)
    if write: c.commit(); r = cur.lastrowid
    else: r = cur.fetchone() if one else cur.fetchall()
    cur.close(); c.close(); return r

def notify(uid, msg): q("INSERT INTO notifications(user_id,message) VALUES(%s,%s)", (uid, msg), write=True)
def log(action): q("INSERT INTO activity_logs(user_id,action) VALUES(%s,%s)", (session.get("uid"), action), write=True)
def tm(v): return (datetime.datetime.min + v).strftime("%H:%M") if isinstance(v, datetime.timedelta) else (v or "")

def roles(*allowed):
    """Backend permission check for every protected route."""
    def deco(f):
        @wraps(f)
        def w(*a, **k):
            if "uid" not in session: return redirect(url_for("login"))
            if allowed and session["role"] not in allowed: abort(403)
            return f(*a, **k)
        return w
    return deco

MENU = {
 "volunteer": [("Browse Events","home"),("My Registrations","my_regs"),("My Availability","availability"),("My Tasks","my_tasks"),("Notifications","notes")],
 "organiser": [("Manage Events","org_events"),("Create Event","event_form"),("Notifications","notes")],
 "coordinator": [("Volunteer Directory","coord_vols"),("Task Assignment","assign"),("Assignment Overview","overview"),("Unfilled Positions","unfilled"),("Scheduling Conflicts","conflicts"),("Notifications","notes")],
 "supervisor": [("My Events","sup_events"),("Notifications","notes")],
 "it": [("User Management","it_users"),("Activity Logs","it_logs")]}
@app.context_processor
def inject(): return dict(menu=MENU.get(session.get("role"), []), session=session)
def page(title, **kw): return render_template("page.html", title=title, **kw)
@app.errorhandler(403)
def forbidden(e): return page("403 - Access denied", text="You do not have permission to do that."), 403

# ---------- public ----------
@app.route("/")
def home():
    s, cat, dt, loc = (request.args.get(k, "") for k in ("s", "category", "date", "location"))
    sql = "SELECT * FROM events WHERE status='open' AND event_date>=CURDATE() AND title LIKE %s AND IFNULL(category,'') LIKE %s AND IFNULL(location,'') LIKE %s"
    args = [f"%{s}%", f"%{cat}%", f"%{loc}%"]
    if dt: sql += " AND event_date=%s"; args.append(dt)
    return render_template("events.html", events=q(sql + " ORDER BY event_date", args))

@app.route("/event/<int:eid>")
def event(eid):
    e = q("SELECT * FROM events WHERE id=%s", (eid,), one=True) or abort(404)
    mine = session.get("uid") and q("SELECT status FROM event_registrations WHERE event_id=%s AND user_id=%s", (eid, session["uid"]), one=True)
    return render_template("event.html", e=e, mine=mine, start=tm(e["start_time"]), end=tm(e["end_time"]))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        n, e, p = (request.form.get(k, "").strip() for k in ("name", "email", "password"))
        if not n or not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", e) or len(p) < 8: flash("Enter a name, valid email and 8+ character password.")
        elif q("SELECT id FROM users WHERE email=%s", (e,), one=True): flash("Email already registered.")
        else:
            uid = q("INSERT INTO users(name,email,password_hash,role) VALUES(%s,%s,%s,'volunteer')", (n, e, generate_password_hash(p)), write=True)
            q("INSERT INTO volunteers(user_id) VALUES(%s)", (uid,), write=True); flash("Account created. Please log in."); return redirect(url_for("login"))
    return page("Register", fields=[("name","Full name","text"),("email","Email","email"),("password","Password (8+ chars)","password")], button="Create account")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        u = q("SELECT * FROM users WHERE email=%s", (request.form.get("email", ""),), one=True)
        if u and u["active"] and check_password_hash(u["password_hash"], request.form.get("password", "")):
            session.clear(); session.update(uid=u["id"], role=u["role"], name=u["name"]); log("login")
            return redirect(url_for(MENU[u["role"]][0][1]))
        flash("Invalid credentials or inactive account.")
    return page("Login", fields=[("email","Email","email"),("password","Password","password")], button="Log in")

@app.route("/logout")
def logout(): log("logout"); session.clear(); return redirect(url_for("home"))

# ---------- volunteer ----------
@app.route("/event/<int:eid>/join", methods=["POST"])
@roles("volunteer")
def join(eid):
    e = q("SELECT * FROM events WHERE id=%s AND status='open'", (eid,), one=True) or abort(404)
    if q("SELECT id FROM event_registrations WHERE event_id=%s AND user_id=%s", (eid, session["uid"]), one=True): flash("You are already registered.")
    elif RULES["ENFORCE_CAPACITY"] and e["capacity"] and q("SELECT COUNT(*) n FROM event_registrations WHERE event_id=%s AND status IN('pending','approved')", (eid,), one=True)["n"] >= e["capacity"]: flash("Event is full.")
    elif not RULES["ALLOW_OVERLAP"] and q("SELECT 1 FROM event_registrations r JOIN events x ON x.id=r.event_id WHERE r.user_id=%s AND r.status IN('pending','approved') AND x.event_date=%s", (session["uid"], e["event_date"]), one=True): flash("You already have an event on that date.")
    else:
        st = "pending" if RULES["REQUIRE_APPROVAL"] else "approved"
        q("INSERT INTO event_registrations(event_id,user_id,status) VALUES(%s,%s,%s)", (eid, session["uid"], st), write=True)
        notify(session["uid"], f"Registration submitted for {e['title']} ({st})."); log(f"registered event {eid}"); flash(f"Registration {st}.")
    return redirect(url_for("event", eid=eid))

@app.route("/my/registrations")
@roles("volunteer")
def my_regs():
    rows = q("SELECT r.id,e.title,e.event_date,r.status FROM event_registrations r JOIN events e ON e.id=r.event_id WHERE r.user_id=%s", (session["uid"],))
    for r in rows:
        if RULES["ALLOW_CANCEL"] and r["status"] in ("pending", "approved"): r["_act"] = [("Cancel", url_for("cancel", rid=r["id"]))]
    return page("My Registrations", cols=[("title","Event"),("event_date","Date"),("status","Status")], rows=rows)

@app.route("/registration/<int:rid>/cancel", methods=["POST"])
@roles("volunteer")
def cancel(rid):
    if not RULES["ALLOW_CANCEL"]: abort(403)
    q("UPDATE event_registrations SET status='cancelled' WHERE id=%s AND user_id=%s", (rid, session["uid"]), write=True); flash("Registration cancelled."); return redirect(url_for("my_regs"))

@app.route("/my/availability", methods=["GET", "POST"])
@roles("volunteer")
def availability():
    if request.method == "POST":
        f = request.form
        if f.get("start_time") and f.get("end_time") and f["start_time"] < f["end_time"]:
            q("INSERT INTO volunteer_availability(user_id,day_of_week,start_time,end_time) VALUES(%s,%s,%s,%s)", (session["uid"], f["day_of_week"], f["start_time"], f["end_time"]), write=True)
        else: flash("End time must be after start time.")
        return redirect(url_for("availability"))
    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    rows = q("SELECT day_of_week,start_time,end_time FROM volunteer_availability WHERE user_id=%s", (session["uid"],))
    for r in rows: r["start_time"], r["end_time"] = tm(r["start_time"]), tm(r["end_time"])
    return page("My Availability", fields=[("day_of_week","Day","select",days),("start_time","From","time"),("end_time","To","time")], button="Add slot",
                cols=[("day_of_week","Day"),("start_time","From"),("end_time","To")], rows=rows)

@app.route("/my/tasks")
@roles("volunteer")
def my_tasks():
    return page("My Assigned Tasks", cols=[("event","Event"),("event_date","Date"),("task","Task")],
        rows=q("SELECT e.title event,e.event_date,t.title task FROM task_assignments a JOIN tasks t ON t.id=a.task_id JOIN events e ON e.id=t.event_id WHERE a.user_id=%s", (session["uid"],)))

@app.route("/notifications")
@roles()
def notes():
    rows = q("SELECT message,created_at FROM notifications WHERE user_id=%s ORDER BY id DESC", (session["uid"],))
    q("UPDATE notifications SET is_read=1 WHERE user_id=%s", (session["uid"],), write=True)
    return page("Notifications", cols=[("message","Message"),("created_at","When")], rows=rows)

# ---------- organiser ----------
@app.route("/org/events")
@roles("organiser")
def org_events():
    rows = q("SELECT e.id,e.title,e.event_date,e.status,e.capacity,(SELECT COUNT(*) FROM event_registrations r WHERE r.event_id=e.id AND r.status IN('pending','approved')) regs FROM events e WHERE organiser_id=%s", (session["uid"],))
    for r in rows: r["_act"] = [("Edit", url_for("event_form", eid=r["id"])), ("Registrations", url_for("org_regs", eid=r["id"]), "get"), ("Delete", url_for("delete_event", eid=r["id"]))]
    return page("Manage Events", cols=[("title","Event"),("event_date","Date"),("status","Status"),("regs","Registered"),("capacity","Capacity")], rows=rows)

@app.route("/org/event/new", methods=["GET", "POST"])
@app.route("/org/event/<int:eid>/edit", methods=["GET", "POST"])
@roles("organiser")
def event_form(eid=None):
    old = q("SELECT * FROM events WHERE id=%s AND organiser_id=%s", (eid, session["uid"]), one=True) if eid else {}
    if eid and not old: abort(403)
    if request.method == "POST":
        f = request.form
        if not f.get("title") or not f.get("event_date") or not f.get("capacity", "0").isdigit(): flash("Title, date and numeric capacity are required."); return redirect(request.url)
        vals = (f["title"], f.get("description"), f.get("category"), f.get("location"), f["event_date"], f.get("start_time") or None, f.get("end_time") or None, int(f["capacity"]), f.get("supervisor_id") or None)
        if eid:
            q("UPDATE events SET title=%s,description=%s,category=%s,location=%s,event_date=%s,start_time=%s,end_time=%s,capacity=%s,supervisor_id=%s,status=%s WHERE id=%s", vals + (f.get("status", "open"), eid), write=True)
            for r in q("SELECT user_id FROM event_registrations WHERE event_id=%s AND status IN('pending','approved')", (eid,)):
                notify(r["user_id"], f"Event '{f['title']}' was updated" + (" (CANCELLED)." if f.get("status") == "cancelled" else "."))
        else: q("INSERT INTO events(title,description,category,location,event_date,start_time,end_time,capacity,supervisor_id,organiser_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", vals + (session["uid"],), write=True)
        log(f"saved event {f['title']}"); flash("Event saved."); return redirect(url_for("org_events"))
    sups = [(s["id"], s["name"]) for s in q("SELECT id,name FROM users WHERE role='supervisor'")]
    fl = [("title","Title","text",old.get("title","")),("description","Description","textarea",old.get("description","")),("category","Category","text",old.get("category","")),
          ("location","Location","text",old.get("location","")),("event_date","Date","date",old.get("event_date","")),("start_time","Start","time",tm(old.get("start_time"))),
          ("end_time","End","time",tm(old.get("end_time"))),("capacity","Capacity (0 = unlimited)","number",old.get("capacity",0)),("supervisor_id","Supervisor","select",sups,old.get("supervisor_id"))]
    if eid: fl.append(("status","Status","select",["open","closed","cancelled"],old["status"]))
    return page("Edit Event" if eid else "Create Event", fields=fl, button="Save event")

@app.route("/org/event/<int:eid>/delete", methods=["POST"])
@roles("organiser")
def delete_event(eid):
    if q("SELECT 1 FROM event_registrations WHERE event_id=%s", (eid,), one=True): flash("Cannot delete: event has registrations. Set status to cancelled instead.")
    else:
        q("DELETE FROM tasks WHERE event_id=%s", (eid,), write=True); q("DELETE FROM events WHERE id=%s AND organiser_id=%s", (eid, session["uid"]), write=True); flash("Event deleted.")
    return redirect(url_for("org_events"))

@app.route("/org/event/<int:eid>/registrations")
@roles("organiser")
def org_regs(eid):
    q("SELECT 1 FROM events WHERE id=%s AND organiser_id=%s", (eid, session["uid"]), one=True) or abort(403)
    rows = q("SELECT r.id,u.name,u.email,r.status FROM event_registrations r JOIN users u ON u.id=r.user_id WHERE r.event_id=%s", (eid,))
    for r in rows: r["_act"] = [("Approve", url_for("decide", rid=r["id"], s="approved")), ("Reject", url_for("decide", rid=r["id"], s="rejected"))]
    return page("Volunteer Registrations", cols=[("name","Volunteer"),("email","Email"),("status","Status")], rows=rows)

@app.route("/org/registration/<int:rid>/<s>", methods=["POST"])
@roles("organiser")
def decide(rid, s):
    r = q("SELECT r.*,e.title FROM event_registrations r JOIN events e ON e.id=r.event_id WHERE r.id=%s AND e.organiser_id=%s", (rid, session["uid"]), one=True) or abort(403)
    if s not in ("approved", "rejected"): abort(400)
    q("UPDATE event_registrations SET status=%s WHERE id=%s", (s, rid), write=True); notify(r["user_id"], f"Your registration for {r['title']} was {s}."); return redirect(url_for("org_regs", eid=r["event_id"]))

# ---------- coordinator ----------
@app.route("/coord/volunteers")
@roles("coordinator")
def coord_vols():
    return page("Volunteer Directory & Availability", cols=[("name","Volunteer"),("email","Email"),("avail","Availability")],
        rows=q("SELECT u.name,u.email,IFNULL(GROUP_CONCAT(CONCAT(a.day_of_week,' ',TIME_FORMAT(a.start_time,'%H:%i'),'-',TIME_FORMAT(a.end_time,'%H:%i')) SEPARATOR '; '),'None entered') avail FROM users u LEFT JOIN volunteer_availability a ON a.user_id=u.id WHERE u.role='volunteer' GROUP BY u.id"))

@app.route("/coord/assign", methods=["GET", "POST"])
@roles("coordinator")
def assign():
    if request.method == "POST":
        t, u = request.form.get("task_id"), request.form.get("user_id")
        ok = q("SELECT 1 FROM tasks t JOIN event_registrations r ON r.event_id=t.event_id WHERE t.id=%s AND r.user_id=%s AND r.status='approved'", (t, u), one=True)
        if not ok: flash("Volunteer must have an approved registration for that event.")
        elif q("SELECT 1 FROM task_assignments WHERE task_id=%s AND user_id=%s", (t, u), one=True): flash("Already assigned.")
        else:
            q("INSERT INTO task_assignments(task_id,user_id) VALUES(%s,%s)", (t, u), write=True); notify(int(u), "You were assigned a new task."); log(f"assigned user {u} to task {t}"); flash("Assigned.")
        return redirect(url_for("assign"))
    tasks = [(r["id"], f"{r['title']} - {r['t']}") for r in q("SELECT t.id,e.title,t.title t FROM tasks t JOIN events e ON e.id=t.event_id")]
    vols = [(r["id"], r["name"]) for r in q("SELECT DISTINCT u.id,u.name FROM users u JOIN event_registrations r ON r.user_id=u.id WHERE r.status='approved'")]
    return page("Task Assignment", fields=[("task_id","Task","select",tasks),("user_id","Approved volunteer","select",vols)], button="Assign")

@app.route("/coord/overview")
@roles("coordinator")
def overview():
    rows = q("SELECT a.id,e.title event,t.title task,u.name FROM task_assignments a JOIN tasks t ON t.id=a.task_id JOIN events e ON e.id=t.event_id JOIN users u ON u.id=a.user_id")
    for r in rows: r["_act"] = [("Unassign", url_for("unassign", aid=r["id"]))]
    return page("Assignment Overview", cols=[("event","Event"),("task","Task"),("name","Volunteer")], rows=rows)

@app.route("/coord/unassign/<int:aid>", methods=["POST"])
@roles("coordinator")
def unassign(aid): q("DELETE FROM task_assignments WHERE id=%s", (aid,), write=True); return redirect(url_for("overview"))

@app.route("/coord/unfilled")
@roles("coordinator")
def unfilled():
    return page("Unfilled Positions", cols=[("event","Event"),("task","Task"),("open_slots","Open slots")],
        rows=q("SELECT e.title event,t.title task,t.slots-COUNT(a.id) open_slots FROM tasks t JOIN events e ON e.id=t.event_id LEFT JOIN task_assignments a ON a.task_id=t.id GROUP BY t.id HAVING open_slots>0"))

@app.route("/coord/conflicts")
@roles("coordinator")
def conflicts():
    return page("Scheduling Conflicts (same volunteer, same date)", cols=[("name","Volunteer"),("event_date","Date"),("n","Tasks that day")],
        rows=q("SELECT u.name,e.event_date,COUNT(*) n FROM task_assignments a JOIN tasks t ON t.id=a.task_id JOIN events e ON e.id=t.event_id JOIN users u ON u.id=a.user_id GROUP BY u.id,e.event_date HAVING COUNT(DISTINCT e.id)>1"))

# ---------- supervisor ----------
@app.route("/sup/events")
@roles("supervisor")
def sup_events():
    rows = q("SELECT id,title,event_date FROM events WHERE supervisor_id=%s", (session["uid"],))
    for r in rows: r["_act"] = [("Attendance", url_for("attendance", eid=r["id"]), "get")]
    return page("My Events", cols=[("title","Event"),("event_date","Date")], rows=rows)

@app.route("/sup/attendance/<int:eid>")
@roles("supervisor")
def attendance(eid):
    q("SELECT 1 FROM events WHERE id=%s AND supervisor_id=%s", (eid, session["uid"]), one=True) or abort(403)
    rows = q("SELECT u.id uid,u.name,t.title task,IFNULL(att.status,'Not recorded') status FROM task_assignments a JOIN tasks t ON t.id=a.task_id JOIN users u ON u.id=a.user_id LEFT JOIN attendance att ON att.event_id=t.event_id AND att.user_id=u.id WHERE t.event_id=%s", (eid,))
    for r in rows: r["_act"] = [(s, url_for("mark", eid=eid, uid=r["uid"], s=s)) for s in ("Present", "Absent", "Late")]
    return page("Attendance Management", cols=[("name","Volunteer"),("task","Task"),("status","Attendance")], rows=rows)

@app.route("/sup/attendance/<int:eid>/<int:uid>/<s>", methods=["POST"])
@roles("supervisor")
def mark(eid, uid, s):
    if session["role"] not in RULES["ATTENDANCE_EDITORS"] or s not in ("Present", "Absent", "Late"): abort(403)
    q("SELECT 1 FROM events WHERE id=%s AND supervisor_id=%s", (eid, session["uid"]), one=True) or abort(403)
    q("INSERT INTO attendance(event_id,user_id,status,recorded_by) VALUES(%s,%s,%s,%s) ON DUPLICATE KEY UPDATE status=%s,recorded_by=%s", (eid, uid, s, session["uid"], s, session["uid"]), write=True)
    notify(uid, f"Your attendance was recorded as {s}."); return redirect(url_for("attendance", eid=eid))

# ---------- IT support ----------
@app.route("/it/users")
@roles("it")
def it_users():
    rows = q("SELECT id,name,email,role,active FROM users")
    for r in rows: r["_act"] = [("Deactivate" if r["active"] else "Activate", url_for("toggle", uid=r["id"]))]
    return page("User Management", cols=[("name","Name"),("email","Email"),("role","Role"),("active","Active")], rows=rows)

@app.route("/it/toggle/<int:uid>", methods=["POST"])
@roles("it")
def toggle(uid):
    if uid != session["uid"]: q("UPDATE users SET active=1-active WHERE id=%s", (uid,), write=True); log(f"toggled user {uid}")
    return redirect(url_for("it_users"))

@app.route("/it/logs")
@roles("it")
def it_logs(): return page("System Activity Logs", cols=[("created_at","When"),("user_id","User ID"),("action","Action")], rows=q("SELECT * FROM activity_logs ORDER BY id DESC LIMIT 200"))

if __name__ == "__main__": app.run(debug=True)
