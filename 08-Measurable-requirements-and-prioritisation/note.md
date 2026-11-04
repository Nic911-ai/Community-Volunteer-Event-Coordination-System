B. Requirements 

| ID | Statement | Type | Priority | Source | Rationale | Verification |
|---|---|---|---|---|---|---|
| FR-02 | The system shall allow volunteer to register for an available event. | FR | MUST | Project requirements  and volunteer registration use case | Registration is one of the main functions of the system. | Walk through the registration process and confirm that the volunteer can submit an event registration successfully. |
| NFR-C01 | With over 100 concurrent users accessing a dataset of 500 community events, at least 95% of the event list request shall be complete within 3 seconds. | NFR-Performance | Not-confirmed | Proposal | The system should remain responsive when many volunteers access available events simultaneously. | Run a load test with 100 concurrent users and measure the response time of event-list requests. |
| NFR-C02 | A volunteer using only a keyboard shall be able to complete the event registration, including navigating the form and entering the information and submitting the registration, without requiring a clicking it. | NFR-Accessibility | Not-confirmed | Proposal | Volunteers should be able to use the system without depending any clicking require | Perform a keyboard only walkthrough and check keyboard accessibility. 

2. Explanation
- FR-02 - Volunteer Registration
- A functional requirements because it describes something the system must do.
- The volunteer is the main actor.
- The system allows the volunteer to select an event and submit a registration.
- It can be tested by completing the registration journey.

- NFR-C01 - Performance
- This is a non-functional requirements because it describes how well the system should carry out and perform.
- It shows a measureable conditions if 100 concurent users and over 500 events.
- The expected outcome is that at least 95% of request complete within 3-5 secounds.

- NFR-C02 _ Accessibility
- This is a non-functional requirement because it describes how users should be able to interact with the system.
- It focus on the key-board access.
- The registration journey must be possible without using a mouse.

C. Write and Check measurable NFR candidates


| Candidate ID | Proposed Requirement | Evidence Need | How could it be tested ? |
|---|---|---|---|
| NFR-C01 | Performance | With 100 concurrent users accessing a dataset of 500 community events, at least 95% of event-list requests shall complete within 3-5 seconds, measured using a performance testing tool. |
| NFR-C02 | Accessibility | A volunteer using only a keyboard shall be able to complete the event registration journey, including navigating filling in and submitting the registration form, without requiring any clicking. | 
| NFR-C03 | Privacy | Only authenticated volunteers shall be able to access their own registration details, while authorised event organisers and volunteer 
   

