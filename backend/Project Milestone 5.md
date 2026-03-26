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
| `created_dt`      | `TIMESTAMP`      | DEFAULT CURRENT TIMESTAMP             | Created when             |  
| `updated_dt`      | `TIMESTAMP`      | DEFAULT CURRENT TIMESTAMP ON UPDATE   | Updated when             |

* index on `username, unique: true`
* index on `email, unique: true`


### `trips`

Description: Represents gruop-trip events

| Name              | Type             | Constraints                          | Description                          |
|-------------------|------------------|--------------------------------------|--------------------------------------|
| `id`              | `INT`            | PK, NOT NULL                         | Trip ID                              |
| `trip_name`       | `VARCHAR(255)`   | NOT NULL                             | Name of trip                         |
| `leader_id`       | `INT`            | FK → users(id), NOT NULL             | Created trip (user)                    |
| `start_dt`        | `DATE`           | NOT NULL                             | Trip start date                      |
| `end_dt`          | `DATE`           | NOT NULL, CHECK (end_dt >= start_dt) | Trip end date                        |
| `is_public`       | `BOOLEAN`        | NOT NULL, DEFAULT FALSE              | Visibility flag                      |
| `created_dt`      | `TIMESTAMP`      | DEFAULT CURRENT_TIMESTAMP            | Created when             |
| `updated_dt`      | `TIMESTAMP`      | DEFAULT CURRENT_TIMESTAMP ON UPDATE  | Updated when             |

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
| `created_at`      | `TIMESTAMP`      | DEFAULT CURRENT_TIMESTAMP             | Created when                   |
| `updated_at`      | `TIMESTAMP`      | DEFAULT CURRENT_TIMESTAMP ON UPDATE   | Updated when                   |

* `trip_id` references `trips`
* `user_id` references `users`


### `expenses`

Description: Represents cost entries for trip

| Name              | Type             | Constraints                           | Description
|-------------------|------------------|---------------------------------------|-------------------------------------|
| `id`              | `INT`            | PK, NOT NULL                          | Expense ID
| `trip_id`         | `INT`            | FK → trips(id), NOT NULL              | Trip ID
| `payer_id`        | `INT`            | FK → users(id), NULL                  | Who paid (NULL for estimates)
| `amount`          | `DECIMAL(10, 2)` | NOT NULL                              | Total amount
| `description`     | `VARCHAR(255)`   | NOT NULL                              | Description
| `is_paid`         | `BOOLEAN`        | NOT NULL, DEFAULT FALSE               | Paid flag (Y/N)
| `split_type`      | `VARCHAR(20)`    | NOT NULL, DEFAULT 'equal'             |
| `created_dt`      | `TIMESTAMP`      | DEFAULT CURRENT_TIMESTAMP             | Created when
| `updated_dt`      | `TIMESTAMP`      | DEFAULT CURRENT_TIMESTAMP ON UPDATE   | Updated when

* `trip_id` references `trips`
* `payer_id` references `users`


### `member_expenses`

Description: Joins `memebers` to `expenses`

| Name              | Type             | Constraints                           | Description
|-------------------|------------------|---------------------------------------|-------------------------------------|
| `id`              | `INT`            | PK, NOT NULL                          | member-expense ID
| `expense_id`      | `INT`            | FK → expenses(id), NOT NULL           | Expense ID
| `user_id`         | `INT`            | FK → users(id), NOT NULL              | User that owes expense
| `amount_owed`     | `DECIMAL(10, 2)` | NOT NULL                              | Total amount owed by user
| `percentage`      | `DECIMAL(5, 2)`  | NULL                                  | Percentage
| `is_settled`      | `BOOLEAN`        | NOT NULL, DEFAULT FALSE               | Paid back (Y/N)
| `created_dt`      | `TIMESTAMP`      | DEFAULT CURRENT_TIMESTAMP             | Created when
| `updated_dt`      | `TIMESTAMP`      | DEFAULT CURRENT_TIMESTAMP ON UPDATE   | Updated when

* `expense_id` references `expenses`
* `member_id` references `users`


### `balances`

Description: Historical record of realized payments between users (_i.e._, settled balances)

| Name              | Type             | Constraints                           | Description
|-------------------|------------------|---------------------------------------|-------------------------------------|
| `id`              | `INT`            | PK, NOT NULL                          | Balance ID
| `trip_id`         | `INT`            | FK → expenses(id), NOT NULL           | Trip ID
| `payer_id`        | `INT`            | FK → USERS(id), NOT NULL              | Paid by user
| `payee_id`        | `INT`            | FK → users(id), NOT NULL              | Received-by user
| `amount`          | `DECIMAL(10, 2)` | NOT NULL                              | Total amount
| `created_dt`      | `TIMESTAMP`      | DEFAULT CURRENT_TIMESTAMP             | Created when
| `updated_dt`      | `TIMESTAMP`      | DEFAULT CURRENT_TIMESTAMP ON UPDATE   | Updated when

