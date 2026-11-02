# Community Volunteer & Event Coordination System (Flask + MySQL)
## Setup
1. Install Python 3.10+ and MySQL; then: `pip install -r requirements.txt`
2. Edit `config.py` (MySQL password).
3. Create DB: `mysql -u root -p < schema.sql`
4. Add sample data: `python seed_data.py`
5. Run: `python app.py` and open http://127.0.0.1:5000
## DEV-ONLY test accounts (password `Test1234!`)
org1@test.com, org2@test.com (organiser) | coord1@test.com, coord2@test.com | sup1@test.com, sup2@test.com | it1@test.com | vol1..vol10@test.com
## Business rules: edit `RULES` in config.py (approval, cancel, capacity, overlap, attendance editors). REQUIRE_TASK_TO_ATTEND is documented but not enforced.
## Common errors: "Access denied for user" -> fix config.py password; "Unknown database" -> run schema.sql; ModuleNotFoundError -> pip install -r requirements.txt.
## Not yet built: About/Contact pages, profile editing, charts, role editing, system health page, email/SMS (notifications are in-system only), automated tests (manual checklist in tests/test_cases.md).
