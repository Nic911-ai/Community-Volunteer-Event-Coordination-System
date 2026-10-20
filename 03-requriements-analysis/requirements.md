1. Problem -> Stakeholders -> Elicitation -> Analysis -> Requiremtns

| Stage | Application to the Community Volunteer & Event Coordination System |
|---|---|
| Problem | Volunteer registration, availability, task assignment, and attendance may be managed using seperate tools, making coordination difficult. This is a problem statement to verify, not a confirmed finding. |
| Stakeholders | Volunteer, Event Organiser, Volunteer Coordinator, Event Supervisor, and IT Support. |
| Elicitation | Interview the five stakeholders, review existing forms and spreadsheets, and aboserve how an event is organised. |
| Analysis | Identify repeated problem, clarify unknowns, resolve conflicting needs, and check which requirements are necessary. |
| Requirements | Produce clear functional requiremnts and quality requirements that can be checked or tested. |

2. Classifying Statements

| Statement | Classification | Reason |
|---|---|---|
| Volunteers need clear information about event tasks. | Stakholder Need | It descibes what volunteers need. |
| The system shall allow supervisors to record volunteer attendance. | Candidate Requirement |It describes a fuction the system may need to provide. |
| The system should use a mobile application. | Solution Idea | It proposes a particular type of solution before confirming the need. |
| IT Support needs to manage user permissions. | Stakholder Need | It describes a technical and administrative need. |
| The system shall send an email or message whenever an event is cancelled. | Candidate Requirements | It specifies a possible system behaviour that needs validation. |

3. Requirments Surgery

- The Sytem Should be User-Friendly

| Step | Answer |
| --- | --- |
| Find | "User-friendly" is vague. |
| Diagnose | It does not explain which user, task or what it means. |
| Ask | Can new volunteer able to register for an event wihout help? |
| Repair | A new volunteer should be able to register for an available event without assistance from an administrator. |
| Check | Test whether a ew volunteer can complete registration without assistance. |

- The System Should Notify User Everything About Events.

| Step | Answer |
| --- | --- |
| Find | "Notify users" is unclear. |
| Diagnose | It does not explain the users, the evnet that will trigger a notification or how the notification method. |
| Ask | How should it be receive and which event changes will be important to be notify. |
| Repair | The system shall notify registered volunteers when an event they registered is cancelled or any changes are made. |
| Check | Cancel a test event and verify that its registered volunteers receve the required notification. |

- The System Should Create Events and Assign Volunteers.

| Step | Answer |
| --- | --- |
| Find | The statemnt combines two different functions. |
| Diagnose | Event creation and volunteer assigment may be performed by diffrent authorised user and require diffrent checks. |
| Ask | Who can create events, and who can assign volunteers? |
| Repair | The system shall allow authorised event organisers to create community events. |
| Repair 2 | The system shall allow authorised volunteer coordinators to assign registered volunteers to specific event tasks. |
| Check | Test event creation and task assignment separately using users with correct permissions. |


4. Functional Requirements


| ID | Requirement | Source | How could we verify it? |
| --- | --- | --- | --- |
| FR-01 | The system shall allow volunteers to view available community events, including each event's date, time, location and desciprtion. | Proposed stakeholder need to confirm through volunteer interviews. | Display several sample events and check all required details. |
| FR-02 | The system shall allow registerd volunteers to register for an available community event. | Proposed stakholder confirm through volunteer interviews. | Register test volunteer for an available event and check the registration is recorded. |
| FR-03 | The system shall allow authorised volunteer coordinators to assign registerd volunteers to specific event tasks. | Proposed stakeholders coordinator interviews. | Assign a registered volunteer to ask and verify the assigment appears correctly. |
| FR-04 | The system shall allow authorised event organisers to view list of volunteers registerd for each event. | Evvent Organiser | Check that the organiser can view the correct volunteer list for a selected event. |
| FR-05 | The system shall allow volunteers to provide their availability for community events | Volunteer | Enter a volunteer availability and check the inormation is saved correctly. |
| FR-06 | The system shall allow authorised event supervisors to record volunteer attendance for an event | Event Supervisor | Check test volunteer as present and confirm the attendance record is saved. |
| FR-07 | The system shall allow volunteers to view tasks assigned them for an event | Volunteer | Assign a task volunteer and check the volunteer can view correct task. |
| FR-08 | The system shall notify registerd volunteers when event they registerd is cancelled. | Volunteer,Event Organiser | Cancel a test event and check whether registerd volunteer recive the required notification. 
| FR-09 | The system shall restrict access to system functions according to each user authorised permissions. | IT Support | Log in using diffrent accounts and check each accout can access with its authorised functions. |












