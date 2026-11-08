1.  Requirement or not?

| Statement | What is it? | Why? |
|---|---|---|
| “We need an online booking system.” | Proposed solution | Rather than showing the specific problem or fuction that needs to be explaied. |
| “The technician needs to know what equipment is currently out.” | Need | Information that the technician needs to perform. |
| “The system shall allow an authorised technician to record an equipment return.” | Requirement | A function the system must provide and identifies the authorised user. |
| “We assume all staff have access to the college network.” | Assumption | Something believed to be true but has not yet been confirmed. |
| “The system must comply with the college’s existing security policy.” | Constraint | Rule or restriction that the system must follow when being developed or operated. |

2. Spot the Problems

1. The system shall be very easy to use
- Problems: "very easy to use" is subjective because diffrent users may have different opinions. Is hard to measur and verufy whether the system is easy to use

2. The system shall quickly show available equipment.
- Problems: "Quickly" is ambiguous becasue there is no specific response time given how quick should it be?

3. The system shall allows staff to book, cancel and approve bookings and send reminders.
- Problems: It does not specify which kind of booking can be cancelled.

3. Rewrite One Requirement

- Original: The system shall quickly show available equipment.
- Rewritten requirement(s): The system shall allow an authorised user to select an equipment item and a date to view its availability.
- How Could you verify it? : Select an equipment item and a date, then check if the system displays the availability for the slected equipment and date.

4. College Equipment Booking System Case Study
- A technician says: “I need to know whether a camera is available before I promise it to a lecturer.”

1. What problem or need is behind the statement?
- How should the system display the camera availability, and should the techician be able to check availability for a soecific date?

2. What would you ask the technician to learn more?
- How should the system display the camera availability, and should the techician be able to check availability for a soecific date?

3. Write ONE candidate functional requirement.
- The system shall allow an authorised user to view camera availability for a selected date.

4. Identify ONE quality/security/privacy/accessibility issue that might need investigation.
- The system should ensure that only authorised users can access equipment booking information.

5. How could the candidate requirement be verified?
- Log in as an authorised user, select a camera and a date, and check whether the system displays its availability correctly.

5. Exit Question
- “A good requirement is useful because it clearly explains what the system needs to do and allows developers and stakeholders to understand, implement and verify the expected behaviour.”

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

5. Reflection
Interview representatives from all difrrent stakholder groups and review. 












