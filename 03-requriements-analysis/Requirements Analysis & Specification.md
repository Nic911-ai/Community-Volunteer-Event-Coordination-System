1. Problem → Stakeholders → Elicitation → Analysis → Requirements
2. Is this actually a requirement?

- “People are sometimes unsure whether a camera is available.” : Problem / observation
- “Technicians need to know what equipment is due back.” : Stakeholder need / concern
- “The system shall record the expected return date for each booking.” : Candidate requirement
- “The college should build a mobile app.” : Solution idea
- “We assume all users will have a college login.” : Assumption
- “A lecturer wants reliable availability information before promising equipment.” : Stakeholder need / concern

3. Requirements Surgery Overview

1. Requirement : "The system shall be user-friendly."
- FIND: Users should be able to use the booking system without unnecessary difficulty.
- DIAGNOSE: "User-friendly" is vague and subjective. It does not identify which users or tasks are being considered. There is no measurable way to check it.
- ASK: Which tasks should students and lecturers be able to complete easily?
- REPAIR: The system shall allow a student or lecturer to view the equipment catalogue and open the details of a selected equipment item.
- CHECK: Ask a test user to find an equipment item and open its details. Record whether the user can complete the task and any problems.

2. Requirement: "The system shall notify users about bookings."
- FIND: Users may need information about events or changes relating to their bookings.
- DIAGNOSE: It does not identify which users receive notifications. It does not state what event triggers a notification. It does not explain what information the notification contains.
- ASK: At which stages of the booking process should users receive notifications?
- REPAIR: Do not finalise this requirement until the notification triggers, recipients and delivery method are confirmed.
- CHECK: Once notification rules are agreed, test each specified event and check that the correct recipient receives the expected message through the agreed method.

3. Requirement: "The system shall allow staff to create, edit and delete bookings and send reminders."
- FIND: Staff may need to manage booking records and communicate with users.
- DIAGNOSE: It does not identify which staff roles can perform each action and when a booking may be edited or deleted. Who receives reminders or when they are sent.
- ASK: Which staff roles can create, edit or delete bookings, and what events should trigger reminders?
- REPAIR: The system shall allow an authorised staff member to review a submitted booking request and record an approval or rejection decision.
- CHECK: Submit a test request, sign in as an authorised staff member and check whether an approval or rejection decision can be recorded. leaves out important conditions and details.
- WHO?: An authorised user, such as a technician or Equipment Manager.Exact roles need confirmation.
- WHAT?: Display equipment availability.
- WHEN?: When the user selects equipment and a date.
- WHY?: To check availability before making a booking commitment.
- HOW WILL WE KNOW?: The system shall allow an authorised user to view equipment availability for a selected date.


3. Develop Functional Requirements


| ID | Requirement | Source | How could we verify it? |
|---|---|---|---|
| FR-01 | The system shall allow an authorised user to view equipment availability for a selected date. | Technician's need	| Select an equipment item and date and check that its availability is displayed. |
| The system shall allow a student or lecturer to submit a booking request for one equipment item by providing a start date and end date.	| College Equipment Booking System case information	| Log in as a student or lecturer, enter an equipment item and booking dates, and check that the request is submitted. |
| The system shall allow authorised staff to review a submitted booking request and record an approval or rejection decision.	| College Equipment Booking System case information	| Log in as authorised staff, review a submitted request and check that an approval or rejection decision can be recorded. |

4. Review the Functional Requirements

- The system shall allow an authorised user to view equipment availability for a selected date.
1. Is the required behaviour clear? : Yes
2. Who is involved? : Authorised user
3. Have we assumed something we do not know? : The meaning of authorised user needs confirmation.
4. Is anything important missing? : How availability is calculated.
5. How could we verify it? : Check displayed availability.

5. Quality requirements


| ID	| Quality requirement	| Why does it matter?	| How could it be checked? |
|---|---|---|---|
| NFR-01	| The system shall require users to log in before accessing booking information. | This helps protect students' and staff members' booking information from unauthorised access. | Attempt to access booking information without logging in and check that access is denied. |

6. Reflection
1. What makes a requirement difficult to understand?

- A requirement is difficult to understand when it uses vague words, combines several functions, does not identify the users involved or leaves out important conditions and details.

2. What information do you still need for your project?

- I still need to know what happens when equipment is unavailable, what information users must provide when submitting a booking request, and which staff roles are responsible for reviewing and deciding on requests.

3. Who could provide that information?

- The Equipment Manager and Department Administrator could clarify equipment availability and booking procedures. Students and lecturers could explain what information they need when making a booking request. IT could clarify authentication, access control and technical requirements.


