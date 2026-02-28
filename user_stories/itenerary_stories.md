# User Stories for Itinerary Page

## Adding an activity
As a trip member I want to add an activity so I can keep track of who is doing what and when.

### Acceptance Criteria
Given: A member has a new activity to add.
When: They click the "Add Activity" button and submit the form with a title ("Hiking"), type ("Activity"), start time/day, and duration (" Day 1 8:00am for 2 hours").
Then: The system saves the record (with a POST request update to activities table?).

## Editing an activity
As a trip member I want to update my activity so I can change the details and keep it current.

### Acceptance Criteria
Given: A member wants to update an activity.
When: They click the "Edit Activity" button and edit the form with updated details (form is pre-filled with current data).
Then: The system saves the record (with a PUT request update to activities table?).

## Deleting an activity
As a trip member I want to delete my activity so I can keep the trip current in case plans change or someone flakes.

### Acceptance Criteria
Given: A member wants to delete an activity in case someone flakes or plans change.
When: They click the "Delete Activity" button and edit the form with updated details (form is pre-filled with current data).
Then: The system saves the record (with a post request update to activities table?).

## Viewing itinerary
As a trip member I want view my trip by date and time so I can visualize the flow.

### Acceptance Criteria
Given: Activities have been added.
When: A member wants to view the trip's schedule.
Then: The page will display the activities starting at the first day of the trip cronologically with each day labeled.

## Categorizing activity
As a trip member I want to put my activity in a category so I can quickly view what types of activities I have and restrict what people can add.

### Acceptance Criteria
Given: A member has a new activity to add or update.
When: They choose a prefilled option for an activity type (domain restrictions if easy).
Then: The member will be able to view the activities in a certain category.

## Members attending activity (reach)
As a trip member I want to add trip members to an activity.

### Acceptance Criteria
Given: A member has a new activity to add or update.
When: They select the member(s) from a list of exisitng trip members (attached to members table)
Then: The member will be able to view the members participating in an activity.

## Tracking activity status (reach)
As a trip member I want to see if an activity has passed.

### Acceptance Criteria
Given: A member views an activity.
When: An activity has passed.
Then: The activity will be grayed out.
