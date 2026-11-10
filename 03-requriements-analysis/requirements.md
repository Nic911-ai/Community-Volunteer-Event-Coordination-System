1. Information from Week 2


| Stakeholder	| Needs	| Concerns |
|---|---|---|
| Volunteer	| Browse events, register and receive event information.	| Complicated registration and too many notifications.|
| Event Organiser	| Create events and manage volunteer registrations.	| Not having enough volunteers or last-minute cancellations. |
| Volunteer Coordinator	| View volunteer availability and coordinate task assignments.	| Difficulty coordinating volunteers and tasks. |
| Event Supervisor	| View assigned volunteers and monitor attendance.	| Missing volunteers or inaccurate attendance information. |
| IT | Maintain the system and manage technical issues.	| System reliability, security and user access. |

Problem statement:
Community events require volunteers, organisers and coordinators to communicate and manage event information. Without a centralised coordination system, it may be difficult to manage volunteer registrations, assign tasks, monitor attendance and communicate event updates.

2. Candidate Requirements


| ID	| Candidate requirement	| Source |
| CR-01	| The system should allow volunteers to browse community events.	| Volunteer |
| CR-02	| The system should allow volunteers to register for community events.	| Volunteer |
| CR-03	| The system should allow volunteers to view their registrations.	| Volunteer |
| CR-04	| The system should allow Event Organisers to create and update events.	| Event Organiser |
| CR-05	| The system should allow Volunteer Coordinators to assign volunteers to tasks.	| Volunteer Coordinator |
| CR-06	| The system should allow Event Supervisors to record volunteer attendance.	| Event Supervisor |
| CR-07	| The system should provide event updates to volunteers. | Volunteer / Event Organiser |



3. Requirements Surgery
FIND → DIAGNOSE → ASK → REPAIR → CHECK


Requirement 1: "The system shall be user-friendly."
- Find: The system should be easy for volunteers and organisers to use.
- Diagnose: "User-friendly" is vague and cannot be directly measured.
- Ask: What tasks should users be able to complete easily?
- Missing information: User experience expectations, accessibility needs and common user difficulties.
- Repair: The system shall allow volunteers to browse community events and access event details through the main navigation.
- Check: Test whether volunteers can locate and open an event through the navigation.

Requirement 2: "The system shall notify users about events."
- Find: Users need information about event updates.
- Diagnose: It does not specify who receives notifications or what triggers them.
- Ask: Which event updates should volunteers receive, and how should they be notified?
- Missing information: Notification types, delivery method, timing and user preferences.
- Repair: The system shall provide volunteers with event update notifications when an event's information is changed.
- Check: Change an event's information and verify whether the relevant notification is provided.
Candidate requirement — needs confirmation

Requirement 3: "The system shall allow staff to create, edit and delete events and send reminders."
- Find: Organisers need to manage events and communicate with volunteers.
- Diagnose: "Staff" is unclear because the project has different staff roles. The reminder process is also unspecified.
- Ask: Which roles are authorised to create, edit or cancel events, and who is allowed to send reminders?
- Missing information: User permissions, cancellation rules and reminder timing.
- Repair: The system shall allow authorised Event Organisers to create and update community events.
- Check: Log in with an Event Organiser account and verify that event creation and updating are available.
Requirement selected for improvement: Requirement 3, because it identifies a specific stakeholder role and a clear system action.


4. Functional Requirements


| ID	| Requirement	Source	| How to verify |
|---|---|---|
| FR-01	| The system shall allow volunteers to browse available community events. |	Volunteer	Open the event listing and check that event information is displayed. |
| FR-02	| The system shall allow a volunteer to register for an available community event.	| Volunteer	Complete and submit a registration form and check that the registration is recorded. |
| FR-03	| The system shall allow authorised Event Organisers to create and update community events.	| Event Organiser	Log in as an Event Organiser and test event creation and updating. |


5. Quality Requirements
   
| ID	| Quality requirement	| Why does it matter?	| How could it be checked? |
|---|---|---|---|
| NFR-01	| The volunteer registration journey shall be usable using only a keyboard, without requiring a mouse.	| Supports users who navigate using a keyboard.	| Test browsing, completing and submitting the registration form using only a keyboard. |


6. Project Application

1. Step 1 — Identify the source: Who provided the information or need?

- Volunteer stakeholder
2. Step 2 — Examine the requirement: What type of requirement is it? Is anything unclear?

- Functional requirement where volunteers need a way to register for community events.
3. Step 3 — Ask a question: What question would you ask the stakeholder to clarify it?

- Does a volunteer's registration become confirmed immediately, or must an Event Organiser or Volunteer Coordinator approve it?
4. Step 4 — Think about verification: How might you know whether the requirement has been satisfied?

- Submit a registration and check whether the system records it correctly.
5. Step 5 — Record an unknown: What information do you still need? Who could provide that information?

- Registration approval process, capacity limits and mandatory registration fields. Volunteer, Event Organiser and Volunteer Coordinator can provide that information.

7. Reflection

1. What makes a requirement difficult to understand?

- A requirement is difficult to understand when it uses vague words, does not identify the user or does not clearly explain what the system should do.

2. What information do you still need for your project?

- I still need information about mandatory volunteer registration fields, event capacity, registration approval, cancellation rules and notification methods.

3. Who could provide that information?

- Volunteers, Event Organisers and Volunteer Coordinators could provide information about registration and event coordination. Event Supervisors could clarify attendance requirements, while IT Support could provide information about technical and security requirements.












