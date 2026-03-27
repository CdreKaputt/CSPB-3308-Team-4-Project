## Project Milestone 3: Weekly Status Report

**Team #:** 4  
**Project:** Flake   
**Team Name:** Mountain Hackers  
**Report Link:** https://github.com/CdreKaputt/CSPB-3308-Team-4-Project/blob/main/meeting_notes/WEEKLY_STATUS_03_12_26.md

---

## Reporting Period

**Week:** 8 
**Meeting Held:** Yes  
**Meeting Date:** March 12, 2026  
**Meeting Duration:** 61 minutes  
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
- **Status Update:** Spencer is slated to clean up the Trello board this 
  Saturday, moving completed wireframe and user story tasks to "Complete" and 
  creating new cards for the pivot to Jinja2 templates and remaining backend 
  routes.

![trello-board-snapsoht](https://github.com/user-attachments/assets/4d63ded8-5a61-45cc-a7a3-3f92b24ab2db)

---

## Progress Since Last Week

This week, the team focused on **establishing core authentication functionality and evaluating front-end framework feasibility**. 
The team successfully demonstrated a working end-to-end auth flow and made a 
strategic decision to prioritize project stability by pivoting from React to 
traditional HTML templates.

Key accomplishments include:
- **Functional Auth Prototype:** Spencer demonstrated a working login, signup, 
  and logout flow using a decoupled backend/frontend architecture.
- **Backend Infrastructure:** Aaron completed the authentication middleware and 
  initial error handling for API routes.
- **Strategic Alignment:** The team unanimously decided to move forward with 
  **Jinja2 templates** instead of React to stay aligned with course curriculum 
  and reduce complexity.

---

## Completed Tasks
- Demo of React/Flask authentication integration
- Initial authentication middleware and route protection
- Milestone 4 wireframe and design documentation
- Lab 7 database preparation (Yan)

---

## Planned Tasks for Next Week
- **Backend Refactoring:** Convert JSON-rendering routes to support template 
  rendering (Spencer).
- **Project Structure:** Create initial file structure for remaining 
  trips/models routes (Aaron).
- **SQL Schema:** Review and finalize the database schema and constraints for 
  Milestone 5 (Joshua).
- **Documentation:** Create a "blueprint" guide for building pages from backend 
  to frontend (Spencer).

---

## Blockers and Issues
[IF BLOCKERS REPLACE LINE BELOW, ELSE REMOVE THIS LINE]
No major technical blockers were encountered this week, though the team noted 
some minor challenges with Flask's error handling patterns compared to other 
frameworks.

---

## Risks and Mitigation
**Identified Risk:** Scope creep or learning curve delays associated with a 
decoupled React frontend.  
- *Mitigation:* The team mitigated this risk by pivoting to traditional 
  server-side rendering (Jinja2 templates) while keeping the API structure as a 
  "reach goal" to allow for future React integration if time permits.

---

## Team Reflection
The team reported:
- High satisfaction with the current progress of the backend and the clarity of 
  the database schema.
- Relief regarding the decision to simplify the frontend stack, which allows 
  members to focus on core functionality.   

The team feels technically sound and ahead of schedule on the database design, 
with a clear roadmap for individual contributions over the coming weeks.

---

## Stand Up/ndividual Contributions This Week
**Aaron Brunswig:** 
+ What I did this week: Developed authentication middleware, worked on backend 
  error handling, and handled Milestone 4 submissions.
+ What I plan to do next week: Create the file structure for remaining 
  routes/models and implement backend logic for trips.
+ Roadblocks: Time constraints and minor Flask-specific implementation hurdles.
**Yan Gu:**
+ What I did this week: Focused on Lab 7 (Database) and Lab 8 (HTML/CSS) to 
  prepare for Milestone 5 and the overview page design.
+ What I plan to do next week: Coordinate with the team on asynchronous meeting 
  options for Spring Break and begin implementing the Overview page.
+ Roadblocks: Managing dependencies between the overview page and other database 
  tables.
**Spencer Iascone:**
+ What I did this week: Built a React prototype for testing the backend, 
  demonstrated full auth flow, and drafted the initial database schema in the 
  wiki.
+ What I plan to do next week: Refactor backend routes for Jinja2 templates and 
  create step-by-step documentation for the team.
+ Roadblocks: Heavy workload next week, though no new school material.
**Joshua Morrison:** 
+ What I did this week: Developed wireframes for the pack list and recorded the 
  weekly meeting/transcript.
+ What I plan to do next week: Lead the SQL schema design (Milestone 5) and 
  serve as Scrum Master.
+ Roadblocks: None reported.
**London Walker:** 
+ What I did this week: Reviewed the backend branch and wiki 
  routes to inform design page work (reported via email).
+ What I plan to do next week: Review meeting decisions and align design work 
  with finalized SQL design.
+ Roadblocks: None reported.

---

## Notes
- Next week's meeting (during Spring Break) will be held **asynchronously via Slack**. 
  Members will post their updates by Thursday.
- Joshua has been appointed as the Scrum Master for the upcoming sprint.