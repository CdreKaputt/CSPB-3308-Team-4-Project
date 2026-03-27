# PROJECT 5 MILESTONE: SQL DESIGN

## Project Name: Flake

## Team Information
- **Team Number:** 4  
- **Team Name:** MountainHackers  

### Team Members (All Present)
- Aaron Brunswig
- Yan Gu
- Spencer Iascone
- Joshua Morrison
- London Walker

### `users` 

Description: Signed up users of the application

| Name              | Type             | Constraints                           | Description                         |
|-------------------|------------------|---------------------------------------|-------------------------------------|
| `id`              | `INT`            | PK, NOT NULL                          | Unique user ID                      |
| `username`        | `VARCHAR(80)`    | NOT NULL, UNIQUE                      | Public username                     |
| `email`           | `VARCHAR(100)`   | NOT NULL, UNIQUE                      | User's email                        |
| `first_name`      | `VARCHAR(100)`   | NOT NULL                              | User's first name                   |  
| `last_name`       | `VARCHAR(100)`   | NOT NULL                              | User's last name                    |
| `password_digest` | `VARCHAR(255)`   | NOT NULL                              | Hashed password                     |
| `created_dt`      | `TIMESTAMP`      | DEFAULT CURRENT TIMESTAMP             | Created time                        |  
| `updated_dt`      | `TIMESTAMP`      | DEFAULT CURRENT TIMESTAMP ON UPDATE   | Updated time                        |

* index on `username, unique: true`
* index on `email, unique: true`


### `trips`

Description: Represents group-trip events

| Name              | Type             | Constraints                          | Description                          |
|-------------------|------------------|--------------------------------------|--------------------------------------|
| `id`              | `INT`            | PK, NOT NULL                         | Trip ID                              |
| `trip_name`       | `VARCHAR(255)`   | NOT NULL                             | Name of trip                         |
| `description`     | `TEXT`           | NULL                                 | Description                          |
| `location`        | `VARCHAR(255)`   | NULL                                 | General location                     |
| `leader_id`       | `INT`            | FK → users(id), NOT NULL             | Created trip (user)                  |
| `start_dt`        | `DATE`           | NOT NULL                             | Trip start date                      |
| `end_dt`          | `DATE`           | NOT NULL, CHECK (end_dt >= start_dt) | Trip end date                        |
| `is_public`       | `BOOLEAN`        | NOT NULL, DEFAULT FALSE              | Visibility flag                      |
| `created_dt`      | `TIMESTAMP`      | DEFAULT CURRENT_TIMESTAMP            | Created time                         |
| `updated_dt`      | `TIMESTAMP`      | DEFAULT CURRENT_TIMESTAMP ON UPDATE  | Updated time                         |

* `leader_id` references `users`


## `user_trips` 

Description: Joins `trips` to `users` (many-to-many) with lifecycle tracking

| Name              | Type             | Constraints                           | Description
|-------------------|------------------|---------------------------------------|-------------------------------------|
| `id`              | `INT`            | PK, NOT NULL                          | Membership ID                       |
| `trip_id`         | `INT`            | FK → trips(id), NOT NULL              | Associated trip                     |
| `user_id`         | `INT`            | FK → users(id), NOT NULL              | Member ID                           |
| `status`          | `VARCHAR(20)`    | NOT NULL, DEFAULT 'active'            | active (Y/N)                        |
| `joined_dt`       | `TIMESTAMP`      | DEFAULT CURRENT_TIMESTAMP             | When user joined                    |
| `left_dt`         | `TIMESTAMP`      | NULL                                  | When user left                      |
| `created_at`      | `TIMESTAMP`      | DEFAULT CURRENT_TIMESTAMP             | Created time                        |
| `updated_at`      | `TIMESTAMP`      | DEFAULT CURRENT_TIMESTAMP ON UPDATE   | Updated time                        |

* `trip_id` references `trips`
* `user_id` references `users`


## `items` 

Description: Represents pack list (gear) items associated with the trip and assignment to user responsible for bringing the items

| Name              | Type             | Constraints                           | Description
|-------------------|------------------|---------------------------------------|-------------------------------------|
| `id`              | `INT`            | PK, NOT NULL                          | Membership ID                       |
| `trip_id`         | `INT`            | FK → trips(id), NOT NULL              | Associated trip                     |
| `name`            | `VARCHAR(255)`   | NOT NULL                              | Item name                           |
| `description`     | `TEXT`           | NULL                                  | Item details                        |
| `quantity`        | `INT`            | NOT NULL, DEFAULT 1                   | Number of items needed              |
| `category`        | `VARCHAR(100)`   | NULL                                  | Item category                       |
| `user_id`         | `INT`            | FK → users(id), NOT NULL              | User assigned to bring item         |
| `created_by`      | `INT`            | FK → users(id), NOT NULL              | User who created item               |
| `is_completed`    | `BOOLEAN`        | NOT NULL, DEFAULT FALSE`              | Whether an item has been added      |
| `status`          | `VARCHAR(20)`    | NOT NULL, DEFAULT 'active'            | active (Y/N)                        |
| `joined_dt`       | `TIMESTAMP`      | DEFAULT CURRENT_TIMESTAMP             | When user joined                    |
| `left_dt`         | `TIMESTAMP`      | NULL                                  | When user left                      |
| `created_at`      | `TIMESTAMP`      | DEFAULT CURRENT_TIMESTAMP             | Created time                        |
| `updated_at`      | `TIMESTAMP`      | DEFAULT CURRENT_TIMESTAMP ON UPDATE   | Updated time                        |

* `trip_id` references `trips`
* `assigned_user_id` references `users`
* `created_by` references `users`


### `expenses`

Description: Represents cost entries for trip

| Name              | Type             | Constraints                           | Description
|-------------------|------------------|---------------------------------------|-------------------------------------|
| `id`              | `INT`            | PK, NOT NULL                          | Expense ID                          |
| `trip_id`         | `INT`            | FK → trips(id), NOT NULL              | Trip ID                             |
| `payer_id`        | `INT`            | FK → users(id), NULL                  | User that paid (NULL for estimates) |
| `amount`          | `DECIMAL(10, 2)` | NOT NULL                              | Total amount                        |
| `description`     | `VARCHAR(255)`   | NOT NULL                              | Description                         |
| `is_paid`         | `BOOLEAN`        | NOT NULL, DEFAULT FALSE               | Paid flag (Y/N)                     |
| `created_dt`      | `TIMESTAMP`      | DEFAULT CURRENT_TIMESTAMP             | Created time                        |
| `updated_dt`      | `TIMESTAMP`      | DEFAULT CURRENT_TIMESTAMP ON UPDATE   | Updated time                        |

* `trip_id` references `trips`
* `payer_id` references `users`


### `member_expenses`

Description: Joins `memebers` to `expenses`

| Name              | Type             | Constraints                           | Description
|-------------------|------------------|---------------------------------------|-------------------------------------|
| `id`              | `INT`            | PK, NOT NULL                          | member-expense ID                   |
| `expense_id`      | `INT`            | FK → expenses(id), NOT NULL           | Expense ID                          |
| `user_id`         | `INT`            | FK → users(id), NOT NULL              | User that owes expense              |
| `amount_owed`     | `DECIMAL(10, 2)` | NOT NULL                              | Total amount owed by user           |
| `percentage`      | `DECIMAL(5, 2)`  | NULL                                  | Percentage                          |
| `is_settled`      | `BOOLEAN`        | NOT NULL, DEFAULT FALSE               | Paid back (Y/N)                     |
| `created_dt`      | `TIMESTAMP`      | DEFAULT CURRENT_TIMESTAMP             | Created time                        |
| `updated_dt`      | `TIMESTAMP`      | DEFAULT CURRENT_TIMESTAMP ON UPDATE   | Updated time                        |

* `expense_id` references `expenses`
* `member_id` references `users`

## Data Access Test Cases

### Users Table

<pre>
Use case name:
    Verify user creation with valid data
Description:
    Test creating a new user account in the system
Pre-conditions:
    Username and email do not already exist
Test steps:
    1. Navigate to sign-up page
    2. Enter valid username, email, and password
    3. Submit form
    4. Query database for new user
Expected result:
    User record is successfully created
Actual result:
    User is stored in database with correct fields
Status (Pass/Fail):
    Pass
Notes:
    N/A
Post-conditions:
    New user exists in database and can log in
</pre>


### Trips Table

<pre>
Use case name:
    Verify trip creation
Description:
    Test creating a new trip with valid inputs
Pre-conditions:
    User is authenticated
Test steps:
    1. Navigate to create trip page
    2. Enter trip details (name, dates, location)
    3. Submit form
    4. Query database for new trip
Expected result:
    Trip is successfully created
Actual result:
    Trip appears in database with correct values
Status (Pass/Fail):
    Pass
Notes:
    N/A
Post-conditions:
    Trip exists and is linked to creator
</pre>


### User-Trips Table

<pre>
Use case name:
    Verify user added to trip
Description:
    Test adding a user as a member of a trip
Pre-conditions:
    Trip and user both exist
Test steps:
    1. Add user to trip
    2. Query user_trips table
Expected result:
    New membership detail is created
Actual result:
    User appears as member of trip
Status (Pass/Fail):
    Pass
Notes:
    None
Post-conditions:
    User is associated with trip
</pre>


### Items Table

<pre>
Use case name:
    Verify item assigned to user
Description:
    Test assigning a pack list item to a user
Pre-conditions:
    Item exists and user is part of trip
Test steps:
    1. Assign item to user
    2. Query item record
Expected result:
    `assigned_user_id` is updated to user
Actual result:
    Item is correctly assigned to user
Status (Pass/Fail):
    Pass
Notes:
    N/A
Post-conditions:
    Item is assigned to user
</pre>


### Expenses Table

<pre>
Use case name:
    Verify expense creation
Description:
    Test adding a new expense to a trip
Pre-conditions:
    Trip exists
Test steps:
    1. Create expense with amount and description
    2. Query expenses table
Expected result:
    Expense is successfully created
Actual result:
    Expense appears in database
Status (Pass/Fail):
    Pass
Notes:
    N/A
Post-conditions:
    Expense is linked to trip and visible in expense list
</pre>
