# Run AFTER schema.sql:  python seed_data.py   (DEVELOPMENT-ONLY test accounts, password: Test1234!)
import mysql.connector, datetime as d
from werkzeug.security import generate_password_hash
from config import DB
c = mysql.connector.connect(**DB); cur = c.cursor(); pw = generate_password_hash("Test1234!")
def user(n, e, r):
    cur.execute("INSERT INTO users(name,email,password_hash,role) VALUES(%s,%s,%s,%s)", (n, e, pw, r))
    if r == "volunteer": cur.execute("INSERT INTO volunteers(user_id) VALUES(%s)", (cur.lastrowid,))
    return cur.lastrowid
org = [user("Olivia Organiser", "org1@test.com", "organiser"), user("Oscar Organiser", "org2@test.com", "organiser")]
for i in (1, 2): user(f"Cathy Coordinator {i}", f"coord{i}@test.com", "coordinator")
sup = [user(f"Sam Supervisor {i}", f"sup{i}@test.com", "supervisor") for i in (1, 2)]
user("Ian IT", "it1@test.com", "it")
vols = [user(f"Volunteer {i}", f"vol{i}@test.com", "volunteer") for i in range(1, 11)]
evs = [("Beach Clean-up","Environment","Dublin Bay"),("Food Bank Drive","Charity","Community Hall"),("Charity 5K Run","Sport","Phoenix Park"),
       ("Senior Tech Help Day","Education","Public Library"),("Community Garden Planting","Environment","Green Lane Garden")]
for i, (t, cat, loc) in enumerate(evs):
    cur.execute("INSERT INTO events(organiser_id,supervisor_id,title,description,category,location,event_date,start_time,end_time,capacity) VALUES(%s,%s,%s,%s,%s,%s,%s,'09:00','13:00',8)",
        (org[i%2], sup[i%2], t, f"Join us for {t}.", cat, loc, d.date.today()+d.timedelta(days=7*(i+1))))
    eid = cur.lastrowid
    for tt in ("Setup crew", "Registration desk"): cur.execute("INSERT INTO tasks(event_id,title,slots) VALUES(%s,%s,2)", (eid, tt))
cur.execute("INSERT INTO event_registrations(event_id,user_id,status) VALUES(1,%s,'approved'),(1,%s,'approved'),(1,%s,'pending')", tuple(vols[:3]))
cur.execute("INSERT INTO task_assignments(task_id,user_id) VALUES(1,%s)", (vols[0],))
cur.execute("INSERT INTO attendance(event_id,user_id,status,recorded_by) VALUES(1,%s,'Present',%s)", (vols[0], sup[0]))
c.commit(); print("Seeded.")
