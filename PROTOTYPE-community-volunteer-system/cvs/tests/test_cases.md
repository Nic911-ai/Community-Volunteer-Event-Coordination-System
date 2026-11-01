| # | Test | Steps | Expected |
|---|------|-------|----------|
| 1 | Register | /register with new email, 8+ char password | Redirect to login; hashed password stored |
| 2 | Bad login | Wrong password | "Invalid credentials" message |
| 3 | Login/logout | vol1@test.com / Test1234! then Logout | Role menu shown, then public home |
| 4 | Role access | As vol1 open /org/events | 403 page |
| 5 | Create/edit event | org1: Create Event, then Edit | Event listed; registered volunteers notified on edit |
| 6 | Register | vol4: open event 1, Register | Status "pending" + notification |
| 7 | Duplicate | Register again | "already registered" |
| 8 | Approve | org1: Registrations > Approve | vol4 approved + notification |
| 9 | Availability | vol1: add slot | Shown in table and coordinator directory |
| 10 | Assign | coord1: Task Assignment | Appears in volunteer's My Tasks; unapproved volunteers rejected |
| 11 | Attendance | sup1: Attendance > Present | Saved + notification |
| 12 | Unauthorised | sup2 opens /sup/attendance/1 | 403 |
| 13 | IT | it1: deactivate vol10 | vol10 login blocked; log entry shown |
