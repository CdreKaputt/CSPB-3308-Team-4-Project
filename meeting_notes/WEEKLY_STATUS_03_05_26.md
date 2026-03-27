## Project Milestone 3: Weekly Status Report

**Team #:** 4  
**Project:** Flake   
**Team Name:** Mountain Hackers  
**Report Link:** https://github.com/CdreKaputt/CSPB-3308-Team-4-Project/blob/main/meeting_notes/WEEKLY_STATUS_03_05_26.md

---

## Reporting Period

**Week:** 7 
**Meeting Held:** Yes  
**Meeting Date:** March 5, 2026  
**Meeting Duration:** 55 minutes  
**Meeting Format:** Zoom 

---

## Overview
This document captures the **weekly status** of the Flake project for the 
specified reporting period.  

It is intended to provide a concise snapshot of progress, plans, and risks, and 
will be added weekly throughout the project.

---

## Project Management Snapshot
The team is using a shared **Trello board** to manage tasks and sprint progress.  
At the time of this report:
- Link: https://trello.com/b/3vxc9cLW/flake-cspb-3308-team-4-project
- Columns include: Backlog, In Development, Ready for Review, In Review, 
  Deployed or Complete
- Tasks are assigned to individual team members or pairs

![trello-board-snapsoht](https://github.com/user-attachments/assets/4d63ded8-5a61-45cc-a7a3-3f92b24ab2db)

---

## Progress Since Last Week

This week, the team focused on **transitioning from high-level user stories to technical page specifications and backend architecture**. 
The team clarified the distinction between wireframes and finalized designs in 
Figma while establishing a boilerplate for a stateless API.

Key accomplishments include:
- Established the `backend_bp` branch with a focus on type safety and explicit 
  model initialization.
- Finalized the 5 core pages for the next milestone: Login, Overview, Itinerary, 
  Cost Splitter, and Pack List.
- Conducted a team-wide Figma workshop to align on design tools and nesting 
  techniques.

---

## Completed Tasks
- Defined individual page assignments for Milestone 4.
- Created and merged "Cost Splitter" user stories and wireframes into main.
- Provided a standardized Markdown template for individual page write-ups to 
  ensure consistency.
- Submitted Milestone 3 documentation incorporating professor feedback.

---

## Planned Tasks for Next Week
- Define all required API routes and document them in the team wiki.
- Complete individual page write-ups (Description, Parameters, Data, Mockups).
- Review the `backend_bp` branch and implement middleware for user 
  authentication.
- Create a README for the backend to explain the structure and route logic.

---

## Blockers and Issues
The team is currently navigating a learning curve regarding specific design and 
development platforms (Figma, Trello). Additionally, there is uncertainty 
regarding the exact tech stack requirements (React vs. Vanilla JS) which needs 
to be verified in the syllabus. 

---

## Risks and Mitigation
**Identified Risk:** Potential project scope creep or technical complexity 
exceeding the current course curriculum (specifically regarding React/State 
management).  
- *Mitigation:* Focus on a "Stateless API" backend that can support either 
  Vanilla JS or React, and prioritize 5 core pages over "nice-to-have" features 
  like Discovery.


---

## Team Reflection
- Appreciation for the internal Figma tutorial which helped demystify the 
  design process for non-designers.
- Positive feedback on the use of Markdown templates to keep deliverables 
  uniform.
- A need for more collaborative "team programming" sessions to reduce isolation 
  while working on complex backend logic.   

The team is successfully moving into the implementation phase with a clear 
division of labor, though ongoing communication is needed to bridge gaps in 
technical familiarity.

---

## Stand Up/ndividual Contributions This Week
**Aaron Brunswig:** 
+ What I did this week: Developed the `backend_bp` branch with type safety; 
  organized the Figma workspace and provided team training; acted as the 
  technical lead for design organization.
+ What I plan to do next week: Serve as Scrum Master; finalize backend README; 
  complete Login page write-up; finalize middleware.
+ Roadblocks: Focusing on clarifying data requirements for the 
  Overview/Dashboard page.
**Yan Gu:**
+ What I did this week: Managed Milestone 3 submission; researched Flask and 
  database schemas to align with project requirements; managed the meeting agenda.
+ What I plan to do next week: Complete the Overview page write-up; meet with 
  Spencer for a user journey walkthrough.
+ Roadblocks: Initial overwhelm with Flask concepts, but currently catching 
    up with course content. 
**Spencer Iascone:**
+ What I did this week: Created Markdown templates for page write-ups; initiated 
  the Team Wiki; finished Cost Splitter user stories; reviewed backend boilerplate 
  logic.
+ What I plan to do next week: Take an initial stab at defining API routes in 
  the Wiki; build temporary testing templates for visual interaction; lead a 
  route-finalization session.
+ Roadblocks: Busy work week, but schedule is stable moving forward.
**Joshua Morrison:** 
+ What I did this week: Focused on onboarding to Figma and Trello; started 
  hand-drawing mockups and drafting Pack List stories.
+ What I plan to do next week: Finish wireframes in Figma using the tools 
  learned today; complete individual page write-up.
+ Roadblocks: Familiarizing self with new design platforms (Figma/Trello).
**London Walker:** 
+ What I did this week: Completed Itinerary user stories and initial wireframes; 
  reviewed peer stories; coordinated with Aaron/Spencer on backend-to-frontend 
  logic.
+ What I plan to do next week: Submit individual write-up early due to absence; 
  continue reviewing existing code.
+ Roadblocks: Unavailable for the next scheduled meeting.

---

## Notes
- The team has agreed to move the "Discovery" page to a lower priority to ensure 
  the 5 core pages are fully functional.
- Aaron will share additional Figma tutorials in Slack and pin them for easy 
  access.
- A "team programming" session is tentatively planned for the weekend to define 
  backend routes collaboratively.