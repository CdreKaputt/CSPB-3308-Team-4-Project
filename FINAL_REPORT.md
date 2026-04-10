# Flake Final Report

## Milestone 8: Final Report Submission

## Project Title
Flake - A Trip Planner for Item Tracking

## Team Members
- Aaron Brunswit
- Yan Gu
- Spencer Iascone
- Joshua Morrison
- London Walker

## Required Links

- Project tracker (instructor can access): [Trello Board](https://trello.com/b/3vxc9cLW/flake-cspb-3308-team-4-project)
- Version control repository (instructors have access): [GitHub Repo](https://trello.com/b/3vxc9cLW/flake-cspb-3308-team-4-project)
- 5-minute customer demo video: [Demo Video](To be added)
- Public deployment site: [StudySync Deployment](To be added)

## Repository Readiness

All team members have verified that their latest work is pushed to the remote repository.

The repository contains the following required files and assets:

- README.md
- WEEKLY_STATUS.md
- PAGE_TESTING.md
- SQL_TESTING.md
- FINAL_REPORT.md
- Project presentation files from the Presentation Milestone
- Video of demo
- Source code (frontend and backend)
- Test cases (unit and integration)
- Source documentation and auto-generated documentation files

## Final Status Report

### What We Completed
- User journey working MVP including:
  - User Sign up and login
  - Create a new trip
  - View an existing trip
  - Add/edit an event associated with a trip
  - Add/edit an expense associated with a trip
  - Other work in progress
- Frontend with a consistent navigation flow
- Backend with REST endpoints
- Database with relational schema in PostgreSQL
- Public deployment of the application
- Project presentation slides
- Customer-facing demo video

### What We Were in the Middle of Implementing
- Trip membership
  - trip creators can add members
  - trip members can leave trips
- Pack List

### What We Planned for the Future
- Auto-reassign cost when a member flakes
- auto-notification of dropped pack items when a member flakes
- Apply React framework to the frontend
- Use API based backend

### Known Problems and Limitations
- TBD: What's not optimized
 
## System Overview

System Architecture: The Flake app uses a standard three-tier architecture:

- Frontend: Flask rendered Jinja2 templates (server-side rendering)
- Backend: Flask / Python3
- Database: SQLAlchemy / PostgreSQL (for local development instance)

Version Control: The team used GitHub version control function for team collaboration
- branch creation for feature development
- pull request and review process in place
- regular branch clear up for version hygien

## Pages That Access Database Information (To be revised)

- Login: users
- Dashboard: users, groups, tasks
- Group Page: groups, group_members, tasks, availability
- Availability Page: availability
- Task Management Page: tasks, users

## Page Data Access Tests (High-Level) (To be revised)

### Use case name
Dashboard loads correct data for the logged-in user

### Description 
Verify the dashboard displays only the logged-in user's groups and tasks.

### Pre-conditions
- User account exists
- User is logged in
- User belongs to at least one group
- User has at least one assigned task

### Test steps
1. Navigate to Dashboard
2. Observe Groups list
3. Observe Tasks Due list

### Expected result
- Groups list includes only groups where the user is a member
- Tasks list includes only tasks assigned to the user (excluding completed tasks)

### Actual result
- Dashboard shows the correct groups and tasks for the user

### Status
Pass

### Notes
N/A

### Post-conditions
No data is modified.

## Reflection

This Flake project gives everyone on Team 4 a 0-to-1 experience building a full-stack web app.
We natigated through all stages of software development lifecycle, including ideation, experince design, system architecturing, implementation, testing, deploying.

Key takeaways: (to be revised)
- Scope control matters. The MVP focus kept the project shippable.
- Frequent integration reduces surprises later.
- Clear task ownership and weekly check-ins kept progress steady.
- Deployment and CI/CD work early paid off during final integration.


