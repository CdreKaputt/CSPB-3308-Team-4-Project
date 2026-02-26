Aaron

## User Story
As a new user, I want to register with a username and password so that I can create an account and access the app.

*Effort Level*
TBD

*Acceptance Criteria*

> Draft — to be confirmed during sprint planning

> Given a username that does not already exist \
> When a `POST` request is made to `/auth/register` with a valid username and password \
> Then a new user record is created in the `users` table \
> And a success response is returned
> 
> Given a username that is already taken \
> When a `POST` request is made to `/auth/register` \
> Then no new record is created \
> And a 409 error is returned with a message indicating the username is unavailable
> 
> Given a request with a missing username or password \
> When a `POST` request is made to `/auth/register` \
> Then a 400 error is returned \
> And the response indicates which field is missing

---

## User Story
As a registered user, I want to log in with my username and password so that I can access the app.

*Effort Level*
TBD

*Acceptance Criteria*

> Draft — to be confirmed during sprint planning

> Given a valid username and password \
> When a `POST` request is made to `/auth/login` \
> Then a session is created for the user \
> And a success response is returned with the user's username
> 
> Given an invalid username or password \
> When a `POST` request is made to `/auth/login` \
> Then no session is created \
> And a 401 error is returned
> 
> Given a request with a missing username or password \
> When a `POST` request is made to `/auth/login` \
> Then a 400 error is returned \
> And the response indicates which field is missing

---

## User Story
As a logged in user, I want to log out so that my session is ended.

*Effort Level*
TBD

*Acceptance Criteria*

> Draft — to be confirmed during sprint planning

> Given an active session \
> When a `POST` request is made to `/auth/logout` \
> Then the session is cleared \
> And a success response is returned
> 
> Given no active session \
> When a `POST` request is made to `/auth/logout` \
> Then a 401 error is returned

---

## User Story
As an unauthenticated user, I want to be blocked from accessing protected API routes so that trip data is kept private.

*Effort Level*
TBD

*Acceptance Criteria*

> Draft — to be confirmed during sprint planning

> Given a request with no active session \
> When any request is made to `/api/v1/...` \
> Then a 401 error is returned \
> And the route handler is never reached
> 
> Given a request with a valid active session \
> When any request is made to `/api/v1/...` \
> Then the request proceeds normally \
> And `g.current_user_id` is available to the route handler

---
