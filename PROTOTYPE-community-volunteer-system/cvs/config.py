# Database settings - EDIT the password to match your MySQL install
DB = dict(host="localhost", user="root", password="your_mysql_password", database="community_volunteer_system")
SECRET_KEY = "change-me-in-production"
# Configurable business rules (change here, restart app)
RULES = dict(
    REQUIRE_APPROVAL=True,     # registrations start as 'pending' until organiser approves
    ALLOW_CANCEL=True,         # volunteers may cancel their registration
    ENFORCE_CAPACITY=True,     # block registration when event is full
    ALLOW_OVERLAP=False,       # allow registering for events on the same date
    REQUIRE_TASK_TO_ATTEND=False,  # (documented; not enforced in this version)
    ATTENDANCE_EDITORS=("supervisor",),  # roles allowed to edit attendance
)
