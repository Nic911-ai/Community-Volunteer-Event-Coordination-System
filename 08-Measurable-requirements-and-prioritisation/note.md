## Lab 8 Measurable requirements and Prioritisation

# A. Evidence check — Community Volunteer & Event Coordination System

- Four confirmed facts

1. The system involves volunteers who can browse and view community events and volunteering opportunities.
2. Volunteers have different roles, skills and availability that are relevant when participating in events.
3. Event organisers need to manage events and ensure that the required volunteer roles are filled.
4. The system involves multiple events, and volunteers may participate in different volunteering opportunities.

- Two open questions

1. Should the system automatically match volunteers to suitable roles based on their skills and availability, or should event organisers manually assign volunteers?
2. Should the system automatically send notifications to volunteers about event updates, cancellations and changes to their assigned roles?

2. Review the Week 7 five-screen prototype

1. Screen 1
– Login / Registration: Volunteers should understand how to access or create an account.

2. Screen 2
– Event Listing : Volunteers should be able to browse available community events.

3. Screen 3
– Event Details : Display event information, required roles, skills and availability requirements.

4. Screen 4
– Volunteer Registration: Clearly communicate that the volunteer has submitted an application or registration.

5. Screen 5
– Confirmation / Dashboard	: Display the registration status and distinguish between submitted, pending review and confirmed participation.

# B. Build an editable seven-field catalogue



| ID | Statement (one concern) | Type | Priority | Source | Rationale | Verfication |
|---|---|---|---|---|---|---|
| FR01 | The system shall allow volunteers to browse and view available community events. | FR | Must | Project case | Volunteers will see volunteering opportunities that they are intrested. | Walk through the event browsing process and confirm that event information is displayed. |
| NFR-C01 | The system shall display the event listing page within 3 seconds for at least 95% of requests when 100 volunteers access the system concurrently. | NFR – Performance | Should |Confirm with stakeholders | Volunteers should be able to browse events without experiencing any delays. | Conduct a load test with 100 concurrent users and record page response times. |
| NFR-C02 | The system shall allow volunteers to complete the event registration process using only a keyboard, without requiring a mouse. | NFR – Accessibility | Should |Confirm with stakeholders | Volunteers who cannot use a mouse should still be able to register for events. | Conduct a keyboard-only walkthrough of the registration process and check against WCAG 2.2 Success Criterion 2.1.1. |


# C. Write and check measurable NFR candidates



| Candidate ID | Proposed requirement | Evidence needed | How could it be tested? |
|---|---|---|---|
| NFR-C01 | Performance | Response-time measurements and load-testing results. | At least 95% of requests complete within 3 seconds. |
| NFR-C02 | Accessibility | Keyboard navigation test results and accessibility walkthrough | All interactive registration controls can be accessed and operated using just keyboard. |
| NFR-C03 | Privacy and Security | User-role permissions, access-control configuration and security test results. | User-role permissions, access-control configuration and security test results. |


# D. Prioritise with a defensible release boundary 


| Item | Priority/Status | Justification or stakeholder question |
|---|---|---|
| Volunteer browses and submits event registration | Must | volunteers need to discover events and express their interest. |
| Event organiser reviews volunteer registrations	| Must | Organisers need to review volunteer registrations to manage participation and fill required event roles. |
| Reminder notification	| Unconfirmed | Notifications volunteers remember upcoming events, but the  delivery method and importance need stakeholder confirmation. |
| Automatic volunteer-role matching | Unconfirmed	| Automatic matching based on skills and availability could improve efficiency, but it is not yet confirmed whether matching should be automated or handled manually by organisers. |


# E. Independent transfer — Campus Workshop Registration  


1. Candidate NFR – Performance
- The system shall display the workshop listing page within 3 seconds for at least 95% of requests when 50 students access the system concurrently.
- Source: Cofirm with stakeholders
- Verification method: Conduct a load test with 50 concurrent students and record the response time for the workshop listing page.

2. Two targeted coordinator questions

1. Capacity: When a workshop reaches its maximum capacity, should the system prevent additional requests, allow requests for staff review, or maintain a waiting list?

2. Quality threshold: What is the acceptable maximum loading time for displaying the workshop listing page when multiple students access the system simultaneously?


# F. Review, consistency and traceability

1. "When 100 volunteers access the event listing page concurrently, at least 95% of requests shall complete within 3 seconds, measured using an automated load-testing tool."

- This condition, measure outcome and verification method are clearly identified.


| Stakeholder need | Requirement | Prototype screen | Intended check |
|---|---|---|---|
| Volunteers need to search community events. | FR01 – The system shall allow volunteers to browse and view available community events. | Screen 2 – Event Listing | Verify that volunteers can view and browse available events. |
| Volunteers need to register for events. | FR02 – The system shall allow volunteers to submit event registration. | Screen 4 – Volunteer Registration | The registration process and confirm that a registration can be submitted. | 
| Organisers need to manage volunteer participation. | FR03 – The system shall allow event organisers to review volunteer registrations. | Organiser Dashboard / Registration Management | Verify that organisers can view submitted registrations. |
| Volunteers need to access the system without a mouse. | NFR-C02 – Keyboard-only registration journey. | Screen 4 – Volunteer Registration | Perform a keyboard-only accessibility only. |



# Reflection 

By reviewing candidate requirements is to ensure that everythig is testable. Some proposed requirements have not yet been confirmed by actual volunteers, event organisers or other relevant stakeholders. Further stakeholder discussions are required to determine whether the proposed requirements accurately reflect their needs and expectations.
























