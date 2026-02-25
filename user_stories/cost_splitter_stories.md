# User Stories and DB Relations for Cost Splitter feature

## User Stories

### 1: Adding an Expense (MVP)

**As a**: Trip member

**I want**: To enter a total expense amount and description

**So that**: The group knows how much was spent and on what.

#### Effort Level: ?

#### Acceptance Criteria: 

**Given**: I am on the Cost Splitter page for a specific trip.

**When**: I input an amount (e.g., $100) and a description (e.g., "Gas, ARCO on 2-22-26").

**Then**: The system saves the expense and associates it with my user ID as the "payer."

---

### 2: Automatic Even Split (MVP)
**As a**: Trip member

**I want**: The system to automatically divide the cost by the number of trip participants

**So that**: I don't have to do the math myself for shared costs.

#### Effort Level: ?

#### Acceptance Criteria: 

**Given**: An expense of $90 is added to a trip with 3 members.

**When**: The expense is saved.

**Then**: The system creates 3 records in the `splits` table, each assigned $30 to a different member.

---

### 3: Balance Overview (MVP)
**As a**: Trip member

**I want**: To see a summary of who owes how much to whom

**So that**: We can settle up at the end of the trip.

#### Effort Level: ?

#### Acceptance Criteria:

**Given**: Multiple expenses have been logged.

**When**: I view the "Overview" section.

**Then**: I see a "Net Balance" (e.g., "You are owed $20" or "You owe $15").

---

### 4: Custom Allocation (Reach Goal)
**As a**: Trip member

**I want**: To "claim" a specific expense or adjust the split percentages

**So that**: Costs like individual meals or specific gas runs are accurately reflected.

#### Effort Level: ?

#### Acceptance Criteria:

**Given**: A $50 gas expense exists.

**When**: I select "Individual Claim" for that expense.

**Then**: The system updates the Expense_Splits so that I owe $50 and all other trip members owe $0 for that specific item.

---

### 5: Real-time Updates
**As a**: Developer

**I want**: The UI to recalculate totals immediately after an expense is deleted or edited

**So that**: Users always see the most accurate financial data.

#### Effort Level: ?

#### Acceptance Criteria:

**Given**: An existing expense of $60.

**When**: I change the amount to $90.

**Then**: The "Net Balance" for all trip members updates instantly without a full page refresh.



## Anticipated Minimum Relations:

### trips

| Column Name   | Datatype        | Constraint/Description              |
|---------------|-----------------|-------------------------------------|
| `id`          | `INT`           | Primary Key, Not Null               |
| `trip_name`   | `VARCHAR(255)`  | not null, Name of trip              |
| `start_date`  | `DATE`          | not null, Start date of trip        |
| `end_date`    | `DATE`          | not null, End date of trip          |
| `created_at`  | `TIMESTAMP`     | Default CURRENT_TIMESTAMP           |
| `updated_at`  | `TIMESTAMP`     | Default CURRENT_TIMESTAMP on update |

### users

| Column Name  | Datatype       | Constraint/Description              |
|--------------|----------------|-------------------------------------|
| `id`         | `INT`          | Primary Key, Not Null               |
| `username`   | `VARCHAR(50)`  | Not Null, Unique                    |
| `email`      | `VARCHAR(100)` | Not Null, Unique                    |
| `first_name` | `VARCHAR(100)` | Not Null                            |
| `last_name`  | `VARCHAR(100)` | Not Null                            |
| `created_at` | `TIMESTAMP`    | Default CURRENT_TIMESTAMP           |
| `updated_at` | `TIMESTAMP`    | Default CURRENT_TIMESTAMP on update |

### memberships (joins table between trips and users)

| Column Name    | Datatype    | Constraint/Description              |
|----------------|-------------|-------------------------------------|
| `id`           | `INT`       | Primary Key, Not Null               |
| `trip_id`      | `INT`       | Foreign Key (Trips.id), Not Null    |
| `member_id`    | `INT`       | Foreign Key (Users.id), Not Null    |
| `created_at`   | `TIMESTAMP` | Default CURRENT_TIMESTAMP           |
| `updated_at`   | `TIMESTAMP` | Default CURRENT_TIMESTAMP on update |

### expenses

| Column Name        | Datatype       | Constraint/Description                                    |
|--------------------|----------------|-----------------------------------------------------------|
| `id`               | `INT`          | Primary Key, Not Null                                     |
| `trip_id`          | `INT`          | Foreign Key (Trips.id), Not Null                          |
| `payer_id`         | `INT`          | Foreign Key (Users.id), Not Null                          |
| `amount`           | `FLOAT`        | Not Null, Total cost of the item                          |
| `description`      | `VARCHAR(255)` | Not Null, (ex: Gas, ARCO on 2/22/26)                      |
| `is_paid`          | `BOOLEAN`      | Default False, True if a member has already paid in full  |
| `expense_type`     | `VARCHAR(20)`  | Not Null, 'actual' (paid), 'estimate' (pre-trip budgt)    |
| `created_at`       | `TIMESTAMP`    | Default CURRENT_TIMESTAMP                                 |
| `updated_at`       | `TIMESTAMP`    | Default CURRENT_TIMESTAMP on update                       |

### splits

| Column Name   | Datatype    | Constraint/Description                                                 |
|---------------|-------------|------------------------------------------------------------------------|
| `id`          | `INT`       | Primary Key, Not Null                                                  |
| `expense_id`  | `INT`       | Foreign Key (Expenses.id), Not Null                                    |
| `member_id`   | `INT`       | Foreign Key (Users.id), Not Null                                       |
| `amount_owed` | `FLOAT`     | Not Null, Member portion of expense - Total Expense / num members - 1  |
| `created_at`  | `TIMESTAMP` | Default CURRENT_TIMESTAMP                                              |
| `updated_at`  | `TIMESTAMP` | Default CURRENT_TIMESTAMP on update                                    |

NOTE: This one will be tricky, calculated when expense is added, updated when a 
      member flakes on trip 