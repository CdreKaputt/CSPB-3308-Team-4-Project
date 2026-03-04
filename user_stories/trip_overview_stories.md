Aaron

## User Story
As a logged in user, I want to retrieve the current trip's basic info so that the overview page can be populated.

*Effort Level*
TBD

 *Acceptance Criteria*

> Draft — to be confirmed during sprint planning
>
> Given an active session \
> When a `GET` request is made to `/api/v1/trip` \
> Then the trip name, destination, start date, and end date are returned
>
> Given no active session \
> When a `GET` request is made to `/api/v1/trip` \
> Then a 401 error is returned

---

## User Story
As a logged in user, I want to retrieve the list of trip members so that the overview page can display who is attending.

*Effort Level*
TBD

*Acceptance Criteria*

> Draft — to be confirmed during sprint planning
>
> Given an active session \
> When a `GET` request is made to `/api/v1/members` \
> Then a list of all trip members is returned including their username and flake status
>
> Given no active session \
> When a `GET` request is made to `/api/v1/members` \
> Then a 401 error is returned

---

## User Story
As a logged in user, I want to retrieve all unassigned pack list items so that the overview page can flag what still needs to be covered.

*Effort Level*
TBD

*Acceptance Criteria*

> Draft — to be confirmed during sprint planning
>
> Given an active session and one or more items with no `claimed_by` value \
> When a `GET` request is made to `/api/v1/items?unassigned=true` \
> Then only items where `claimed_by` is null are returned
>
> Given an active session and all items are assigned \
> When a `GET` request is made to `/api/v1/items?unassigned=true` \
> Then an empty list is returned
>
> Given no active session \
> When a `GET` request is made to `/api/v1/items?unassigned=true` \
> Then a 401 error is returned
