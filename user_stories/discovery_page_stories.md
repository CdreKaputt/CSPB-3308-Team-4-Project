Yan

## User Story

As a user, I want to view a list of trips outside of my own so that I can explore and discover.

*Effort Level*  
Medium

*Acceptance Criteria*

> Given an active session \
> When a `GET` request is made to the discovery page \
> Then the page returns a list of trips marked as public \
> And each trip displays high-level information about it
>
> Given there are no public trips available \
> When a `GET` request is made to the discovery page \
> Then the page still loads successfully \
> (Optional) An empty-state message is shown instead of trip cards



## User Story
As a user, I want the discovery page to show helpful high-level information for each trip so that I can quickly decide which trips are worth learning more.

*Effort Level*  
Medium

*Acceptance Criteria*

> Given a public trip is displayed on the discovery page \
> When the trip card is rendered \
> Then it includes the trip name, start date and end date \
>
> Given multiple public trips exist \
> When the discovery page is loaded \
> Then each trip is shown in a consistent card or list format



## User Story
As a developer, I want the discovery page to show only public trips so that private trip planning remains visible only to invited members.

*Effort Level*  
Low

*Acceptance Criteria*

> Given a mix of public and private trips in the database \
> When the discovery page is loaded \
> Then only trips with `public = true` are included in the results \
> And private trips do not appear anywhere on the page
>
> Given a trip's public flag is changed from true to false \
> When the discovery page is loaded again \
> Then that trip no longer appears in the discover list




## User Story
As a developer, I want the discovery page to reuse the application's shared layout and styling patterns so that user experience feels consistent across the app.

*Effort Level*  
Low

*Acceptance Criteria*

>
> Given a user is on the discovery page \
> When the page is rendered \
> Then the Flake logo and navigation links display correctly \
> The page shares the same global header with other pages \
> And the page-specific content appears inside the shared `home.html` layout
> And their trip-list layout uses the same design language
