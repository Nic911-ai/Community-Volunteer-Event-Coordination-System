1. Stakeholders
- Volunteer
- Event Organiser
- Volunteer Cordinator
- Event Supervisor
- IT

2. Stakeholder needs and concerns

| Stakeholder | Needs | Concerns |
|---|---|---|
| Volunteer | Easy registration, event information, task information, notifications | Complexity, too many notification |
| Event Organiser | Easy event creation, volunteer assignment, attendace information | Missing and last-minute cancellation volunteers. |
| Volunteer Coordinator | Availability information, task assigment, volunteer overview | Availability |
| Event Supervisor | Know who is attending and their roles | Volunteers not showing up or being assigned incorrectly. |
| IT | User and permission management, realiable system, technical support and maintenance | Security, System downtime, techincal problems for all |

3. Unknowns

| Unknown | Who could answer? |
|---|---|
| Do volunteer roles require specific skills or qualification - for example first aid | Event Organiser/Volunteer Cordinator |
| Can volunteers swap or be changed after registering to one event | Event Organiser |
| What types of notifications are required? | Volunteers/Event Organiser/Volunteer Cordinator |
| Should notifications be sent through email,push-notification or the system? | Volunteers/Event Organiser/Volunteer Cordinator |
| What personal information should be stored about volunteers? | Event Organiser/Volunteer Cordinator/IT |
| Who should be allowed to view volunteer information | Volunteers/Event Organiser/Volunteer Cordinator/IT |
| Should volunteers be able to record their volunteer hours? | Event Organiser/Volunteer Cordinator |
| What happens when an event is canceeled?| Event Organiser/Volunteer Cordinator |

4.Information Sources 

| Infromation Source | What We Can Learn |
|---|---|
| Interview with volunteers | Registration error, event inormation needs, notification, last minute cancellation |
| Interview with event organisers | How events are created and structure, how colunteers are assigned and how attendance should be managed |
| Interview with volunteer coordinators | How is managed and collected, how tasks are assigned and how staff gaps are identified. |
| Interview with event supervisors | How attendance is checked and how volunteer responsibilities are monitored. |
| Interview with IT Support | Technical requirements, user access, security, backups and system maintenance. |
| Event schedules | How does event dates, times, locations, and activities are recorded |

6. Elicitation Questions
A. Volunteer
- How do you find about community volunteer events?
- What information do you need before joing an event?
- How would you like to register for an event?
- Would you like to choose your own tasks?
- Should you be allowed to cancel your registration?
- How would you prefer to receive event reminders and updates?
- Which notifications are useful and which would you feel unnecessary?
- What would make you feel the system is difficult or frustrating to use?

B. Event Organiser
- How do you create and manage community events?
- What information must be recorded when creating an event?
- How do you decide how many volunteers are needed?
- How do you assign volunteers to an event?
- How do you handle last-minute cancellation from the volunteers?
- What information do you need to know from the volunteer?
- What should happen if an event is cancelled or changed?
- What event reminders or notifications should be sent?
- Do you need reports showing registration and attendance?
- What is the biggest problem with the current event management process?

C. Volunteer Coordinator
- How do you currently collect volunteer availability?
- How do you decide which volunteer should perform each tasl?
- Should volunteers be able to select their preferred tasks?
- Do same tasks requre particular skills or qualifications?
- How should volunteer cancellations be handled?
- What information do you need from the volunteers?
- What information would help coordinate volunteers more efficiently?

D.Event Supervisor
- How do you currently check whether volunteers have arrived?
- What information do you need about the volunteers assigned to your event?
- Should you be able to view each volunteer's assigned tasks?
- How would you like the attendace be recorded?
- What happen if a voluntter does not show up?
- Do you need to contact volunteers through the system or external system?
- What information should be available to you during an event?

E. IT Support
- What technical requirements must the system meet?
- What personal information should be store in the system?
- Should each stakholders have diffrent access permissions?
- How should user accounts be created, updated and disable?
- What security measures are required?
- How should the system handle errors or downtime?
- How does backups and data recovery be done?
- Who will maintain the system?

7. Example Interview Notes


| Stakholder | Example Finding | Possible Implication |
|---|---|---|
| Volunteer | The volunteer finds out about events through messages and wants all important information | The system may need to display event details clearly. |
| Volunteer | The volunteer wants to know their responsibilities before attending. | The system may need to display assigned tasks. |
| Volunteer | The volunteer may be unavailable after registering. | The system may need a cancelation or withdrawal function. |
| Event Organiser | The organiser uses spreadsheet to track registration | The system may need a centralised registation list |
| Event Organiser | THe organiser has difficulty identifying events with too little volunteers | The system may need to display filled and unfilled position. |
| Volunteer Coordinator | The coordinator needs to know volunteer availability before assigning tasks. | The system may need to record volunteer availability. |
| Volunteer Coordinator | Some event taks may require specific skills. | The need to record skills from volunteers. |
| Event Supervisor | The supervisor needs to know who has arrived and which tasks they are assigned. | The system may need attendance and task information. |
| IT Support | Diffrent users may need diffrent level access. | THe system may need role based permissions. |

8. Candidate Requirements

| Stakeholder Finding | Identified Need | Candidate Reuirement | Validation Question |
|---|---|---|---|
| Volunteers want to see event information before and afrer signing up. | Access to event details. | The system shall allow volunteers to view event dats, times, locations, and desciprtions before registering. | Are any other detila required before a volunteer can register? |
| Organisers need to keep track of coluteer registrations. | Centralised registration management. | The system shall allow authorised event organisers to view the list of volunteers registered for each event. | Which volunteer details should organisers be allowed to view? |
|Coordinators need to know volunteer availability. | Availability management | The system shall allow volunteers to provide their availability for volunteer events. Should availability be recorded for individual dates, time periods or both. |
| Coordinators need to assign volunteers to tasks. | Task assignment. | The system shall allow authorised volunteer coordinators to assign registered volunteer to specific tasks. | Can coordinators reassign volunteers after an assigment has been made? |
| Supervisors need to know who attended an event. | Attendance tracking | They system shall allow authorised event supervisors to record volunteer attendance for an event. | Should attendance include only present/absent status, or also arrival and departure times? |
| Volunteers need information about thier responsibilities. | Access to assigned task details. | The system shall allow volunteers to view their assigned task and responsibilities for an event . | What details should be displayed for each task? |
| Volunteers need to receive importnat event updates. | Registration withdraw | The system shall allow registerd volunteers to withdraw from an event, subject to the organisation's cancellation rules. | What is the cancellation deadline? and what should happen after it is cacnel? |
| Organisers need to manage cancellations. | Registration withdrawal management | The system shall allow registerd volunteers to withdraw from an event, subject to the organisation's cacellation rules. |
| IT Support needs to protect system access. | User access control | The system shall restrict system fuctions according to each user's authorised access permissions. | What permissions should each stakholders have. |
| Organisers neeed to identify events that short of volunteers. | Staffinf visibility. | The system shall display the number of registered volunteers for each event event. | Is the total number enough, or must the system also show unfilled tasks? |


9. Problem -> Stakeholders -> Elicitation -> Analysis -> Requiremtns

| Stage | Application to the Community Volunteer & Event Coordination System |
|---|---|
| Problem | Volunteer registration, availability, task assignment, and attendance may be managed using seperate tools, making coordination difficult. This is a problem statement to verify, not a confirmed finding. |
| Stakeholders | Volunteer, Event Organiser, Volunteer Coordinator, Event Supervisor, and IT Support. |
| Elicitation | Interview the five stakeholders, review existing forms and spreadsheets, and aboserve how an event is organised. |
| Analysis | Identify repeated problem, clarify unknowns, resolve conflicting needs, and check which requirements are necessary. |
| Requirements | Produce clear functional requiremnts and quality requirements that can be checked or tested. |


10. Classifying Statements


| Statement | Classification | Reason |
|---|---|---|
| Volunteers need clear information about event tasks. | Stakholder Need | It descibes what volunteers need. |
| The system shall allow supervisors to record volunteer attendance. | Candidate Requirement |It describes a fuction the system may need to provide. |
| The system should use a mobile application. | Solution Idea | It proposes a particular type of solution before confirming the need. |
| All 


