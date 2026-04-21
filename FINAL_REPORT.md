# Flake Final Report

## Milestone 8: Final Report Submission

## Project Title
Flake - A Trip Planner for Accountability Tracking

## Team Members
- Aaron Brunswit
- Yan Gu
- Spencer Iascone
- Joshua Morrison
- London Walker

## Required Links

- Project tracker (instructor can access): [Trello Board](https://trello.com/b/3vxc9cLW/flake-cspb-3308-team-4-project)
- Version control repository (instructors have access): [GitHub Repo](https://trello.com/b/3vxc9cLW/flake-cspb-3308-team-4-project)
- 5-minute customer demo video: [Demo Video](https://drive.google.com/file/d/1_Sa3SQUnarWKKaqpa3WdMHV6OC2eYeHq/view?usp=sharing)
- Public deployment site: See instructions for local host

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
- MVP Functions are all ready
- Use React framework for frontend

### What We Planned for the Future
- Auto-reassign cost when a member flakes
- auto-notification of dropped pack items when a member flakes
- Apply React framework to the frontend
- Use API based backend

### Known Problems and Limitations
- User experience is not fully consistent. The event page has a slight different look and feel from other pages.
- The confirmation pop-up is a system dialogue that has system message.
 
## System Overview

System Architecture: The Flake app uses a standard three-tier architecture:

- Frontend: Flask rendered Jinja2 templates (server-side rendering)
- Backend: Flask / Python3
- Database: SQLAlchemy / PostgreSQL (for local development instance)

Version Control: The team used GitHub version control function for team collaboration
- branch creation for feature development
- pull request and review process in place
- regular branch clear up for version hygien

## Pages That Access Database Information

- Login: users
- Dashboard: users, trips
- Expenses: expenses, trips
- Events: events, trips, users
- Discover: users, trips
- Item: item, users

## Page Data Access Tests (High-Level) (More use cases to be added)

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

---
### Use case name

Login page

### Description

Verify the login page and the signup pages function as expected

### Pre-conditions

- User is not logged in

### Test steps

- From login page, hit “Sign Up” link
- Fill out form to create new user
- Once redirected back to login, use the new user username and password to log in.
- Confirm that login is successful and user is redirected to /dashboard page.

### Expected result

- Completing the new user form should submit and redirect user back to login page.
- Filling in new user username and password should allow the user to log in.
- Once logged in, the user should be redirected to the dashboard page.

### Actual result

- New user created successfully
- User is able to log in with the new username and password.
- User is redirected to the dashboard as expected

### Status

Pass

### Notes

- The alert message displayed on the log in page after creating a user does not automatically disappear. Refreshing the page will remove it but it shouldn’t prevent the user form filling out the login form and logging in correctly.

### Post-conditions

- New user added to the database  

---
### Use case name

Pack List page

### Description

Verify that the Pack List page correctly displays items associated with a trip and that the new/edit item forms work as intended.

### Pre-conditions

- User account exists
- User is logged in
- User belongs to at least one trip

### Test steps

- Create new trip
- From trip dashboard navigate to the Pack List page
- Create new item and observe status
- Edit item to change name and status to completed
- Delete item

### Expected result
- A new item should be created with the values provided in the new item form.
- The item should be assigned to the current user
- Item should show a “Pending” badge.
- After editing the values and setting the item to complete, the item listed on the Pack List page should use the updated values, be grayed out, and show the “Done” badge on the right indicating that that item has been sourced.
- The delete button should remove the item from the packlist

### Actual result
- Item is created with the expected values and pending badge
- Item is assigned to current user
- Item values update correctly after editing item.
- Marking item as complete results in grayed out text and “Done” badge
- Delete functions as expected

### Status

Pass

### Notes

- There is currently no advanced logic checking the permissions of the current user other than ensuring they are logged in when creating/editing/deleting an item. In theory, any logged in user that is not a member of the trip could still access this page and forms and make changes. This is not an oversight but complex user authorization is a stretch goal and will be added in a later version.
- Currently there is no way to reassign an item to another member, but this will also be added at a later time.

### Post-conditions

- New test trip added and saved in database.
- Item added then removed from database.  

---
### Use case name
Events loads correct information for logged in user  
### Description 
Verify the events page displays events for logged in user’s trip  
### Pre-conditions
- User account exists 
- Trip exists
- User has access to trip page
- At least one event exists  
### Test steps
1. Log in and navigate to the trip dashboard
2. Select a trip
3. Navigate to itinerary from trip page
4. Observe list of events
5. Click on event to navigate to event overview
6. Observe event details  
### Expected result
- Event page shows the trip events associated with the trip
- Event overview shows the event details including the date, title, and description  
### Actual result
- Event page correctly shows the trip events for the user’s trip
- Event overview loads the correct event information  
### Status
Pass  
### Notes
Since user can see any public trips, it is not limited to only trip members  
### Post-conditions
Event data is modified  

---
### Use case name
Discover page

### Description 
Verify the discover page correctly shows all public trips  
### Pre-conditions
- User account exists 
- At least one public trip exist      
### Test steps  
1. User log in
2. Click on "Explore Public Trips" button
3. The link successfully redirects user to the discover page
### Expected result
- A full list of all public trips are shown
- Each trip is contained in a card
- Trip name, description and date are displayed  
### Actual result
- Discover page corretly loaded
- All public trips are listed
- Each trip contained in a card has trip name, description and date correctly displayed    

### Status
Pass
### Notes
None public trips are not listed  
### Post-conditions
No data is modified  

---
### Use case name
Expense page  
### Description 
Verify the user can add and edit expenses associated with a trip

### Pre-conditions
- User has logged in
- User is viewing a trip details
- Expense List button successfully displays  
### Test steps
- Click on the "Expense List" button
- The link redirects user to the expenses page
- Click "Add an Expense" button to create a new expense
  - Provide a Description for a new expense
  - Provide the Amount for that new expense
  - Click "Add Expense" to save that expense
- Click on "Back to Trip Page" to go back
- Click "Edit" to update an expense
  - Update the Description
  - Update the Amount
  - Tick the "Paid" box
- Click "Delete" to delete an expense
  - Click "Cancel" to cancel the deletion
  - Click "OK" to confirm the deletion
### Expected result
- The expense page successfully loads a table of expense
  - Each row has Description, PayerID, Amount, Paid?, Date Added fields
  - Each row has action button of Edit and Delete
- The "Add an Expense" button redirects user to a new page
  - The add expense page allows user to input Expense Description and Amount
  - The "Add Expense" button allows user to save that new expense
  - Once done, redirect user back to expense page
- The "Edit" link redirects user to the expense detail page
  - A checkbox of "Paid" appears
  - "Update Expense" button saves the expense change
  - Cancel redirects user back to the expense list page 
- The "Delete" link pop up a confirmation box
  - The "Cancel" does nothing to the expense
  - The "OK" deletes the expense 
### Actual result
Same as expected  
### Status
Pass
### Notes
The user experience of Delete confirmation dialogue can be improved. Now it's a system dialogue starts with "127.0.0.1:8000 says ..."
### Post-conditions
Expense data has been updated    

## Reflection

This Flake project gives everyone on Team 4 a 0-to-1 experience building a full-stack web app.
We natigated through all stages of software development lifecycle, including ideation, experince design, system architecturing, implementation, testing, deploying.

Key takeaways:  
- Defining clear scope was helpful to keep us on track.
- Having scrum master responsible for Weekly standup meeting helped the team coordinate tasks well.
- Regular slack messages helped us make sure we were all on the same page.
- Make critical tehcnical stack decision helps unblock the team to make continuous progress 

