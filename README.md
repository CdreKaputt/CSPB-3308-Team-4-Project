# Flake

## Team Information

**Team #:**  
*Team #4*

**Team Name:**  
*Mountain Hackers*


## Team Members

| Name            | GitHub     | Email                        |
|:---------------:|:----------:|:----------------------------:|
| Aaron Brunswig  | cdrekaputt | aaron.brunswig@colorado.edu  |
| Spencer Iascone | siascone   | spencer.iascone@colorado.edu |
| Joshua Morrison | morrijos   | joshua.morrison@colorado.edu |
| London Walker   | lochad     | london.walker@colorado.edu   | 

## Weekly Team Meeting

**Day:** Saturday
**Time:** 2:00-2:30 PM
**Time Zone:** Mountain Time (MT)

**Duration:** 30 minutes  
**Platform:** Zoom

## Zoom Links

**2026-02-07:** [Initial Meeting - User Stories](https://drive.google.com/file/d/1G7F5mYXtdbbiQEcYztoqLuwhUYOP90v2/view?usp=sharing)

**2026-02-14:** [Meeting 2 - Project Proposal]() <!-- TODO: Insert meeting 2 recording link and remove this comment -->

## Vision Statement

*A resource application to coordinate logistics for group trips where ***"who is 
in charge of what"*** is the main problem/concern.*

## Motivation

**The Problem:** Group trips often suffer from the Bystander Effect when team 
members assume someone else has it covered. As a result critical gear (stove, 
tents, water filters etc) gets left behind. The cause is almost always 
fragemented communication and last minute cancelations; what we like to call the 
"Flake".

**The Solution:** A web application that supports trip accountability through 
**claimed-item ownership** by team members. Team members can claim 
responsibility for various trip necessaties in a shared *"Pack List"* 
environment as well as track costs and manage the itenerary. If at anytime a 
member *"Flakes"* on the trip, the application updates that team member's 
assigned responsibilities as "Unassigned," triggering a notification to the 
remaining team members that there are trip necessaties unaccounted for.

## MVP (The 5 pages)
1. **Trip Overview:** Countdown timer, location map, attendee list, list of 
   items that still need to be acquired by/assigned to group members
   - Nice-to-Have: include group skill level chart so that the trip can be 
     planned to accommodate all team members (follows second primary 
     mountaineering rule of "never go at the pace of the fastest team member, 
     switch up the lead").

2. **The Pack List:** A shared checklist where users can add/remove and 
   *"claim"* items (ex: Joshua is bringing the stove. London is bringing the 
   cooler. Aaron is bringing the canoes. Spencer is bringing the tents. etc. | 
   items needed: food, lighting, sunblock etc.). CRUD

3. **Itinerary:** An editable day-by-day breakdown of the trip plan. CRUD
   - First created when primary user/group lead creats a trip. 

4. **Cost Splitter:** A simple ledger to track shared expenses (gas, permits, 
   food etc.). User can update the ledger and see cost per person automatically
   adjusted. CRUD

5. **Discovery page:** A page to browse public trip templates or past trips. 
   READ only

6. **Nice-to-Haves:** 
    - Friends 
    - Likes  
    - Star Rating System 
    - Public Events Page

## Risks to Project Completion

- *New Technologies:*
    - Flask and React are new tools for many of us and will require some time to
      familiarize ourselves with.
- *First-Time Team:*
    - As this will be our first time working together there will likely be a 
      small adjustment period as we establish norms for code reviews, version
      control strategies and communication styles.
- *The Post-Work Constraint:*
    - As we are a team of working professionals there is the chance that we will 
      likely run into full-time work constraints that require adjustments to 
      planned task completion timelines.
- *Feature Creep:*
    - There are many aspects of the project that excited discussion in our team
      proposal meeting and with that brings the possibility of focusing on the
      novel over the essential.

## Mitigation Strategy

- *New Technologies Risk Mitigation:*
    - Each team member brings a unique set of skills that can balance and 
      support each of the other team members. This will allow us to use a 
      "Shared Component" practice in our development: a given domain expert can 
      take the lead on the introduction of a new technology and share resources 
      and experiece to bring each other up to speed and help reduce the needed 
      learning time of the team as a whole.
    - Team member skills to be leverage:
        + Design/layout experience
        + Database structure and query experiecne
        + Cloud deployment/management experience
        + Fullstack (React) development experience
- *First-Time Team Risk Mitigation:*
    - We will establish a dedicated *git Flow* practice as well as a baseline 
      of what constitutes *"done"* for any given feature (i.e. establish what 
      the MVP of our project looks like.)
    - We will manage our project timeline and monitor progress through the use of 
      a Trello board to ensure we are staying on track and ensure all team 
      members are aware of what has been completed and what needs to be worked 
      on. 
- *Post-Work Constraint Risk Mitigation:* 
    - We will prioritize an *Asynchronous-First* workflow balanced with a weekly
      stand-up and strategy meeting. 
    - We will prioritize well-documented development so Frontend and Backend 
      work can be done independently without waiting for live meetings.
- *Feature Creep Risk Mitigation:* 
    - We will categorize all project features as *Must-Have* (Course Required) 
      or *Nice-to-Have* (App Polish/Reach). *Must-Have* features must meet MVP
      requirements before *Nice-to-Have* features can be started.

## Development Method

*Project Management Methodology: Modified Scrum*

Structure:
- **Method:** We will utilize a "Modified Scrum" framework. While we cannot 
  commit to the traditional Daily Stand-up due to full-time work schedules, we 
  will maintain the core pillars of Transparency, Inspection, and Adaptation 
  through an emphasis on a "Live" Sprint Board (Trello) and a weekly 
  synchronized meeting.

- **Sprints (1 Week):** Sprints will run from Sunday to Saturday. This aligns 
  with our weekly meeting schedule and allows for a clear "Reset" every weekend 
  to evaluate progress and set new goals for the coming week.

- **Task creation/prioritization:** Tasks are broken down into User Stories 
  (e.g., "As a user, I want to see which gear is unassigned when a member 
  flakes") and added to the Product Backlog. During the weekly Sprint Planning 
  session (the "strategy" portion of our meeting), we will move high-priority 
  stories into the Sprint Backlog based on the 5-page MVP requirements.

- **Progress Review:** Each weekly meeting begins with a 15-minute Synchronized 
  Stand-up where each member reports: What I finished last week, what I’m 
  working on this week, and any blockers. We will conclude each Sprint with a 
  brief Sprint Review to demo functional code followed by a short a Sprint 
  Retrospective to adjust our workflow if scheduling or technical hurdles are 
  slowing us down. 
    - NOTE: All code merged to a deployment branch will need to undergo a 
      review via Pull Request from at least one other team member (idealy two).

- **Work Assignments:** During Sprint Planning, team members will "claim" tasks 
  from the Sprint Backlog that align with their current capacity and learning 
  goals (e.g., a member wanting to learn SQL might pair with a more 
  experienced peer on a Backend ticket). All tasks will have a primary and a 
  secondary team member assigned so that any encountered work or life hurdles 
  may more easily be supported and navigated as a team. All assignments will be 
  tracked via the Flake Trello board.

## Project Tracking Software

Project management will be tracked through the use of a Trello board.

**Tracking tool link:** [Flake Trello Board]() <!-- TODO: Insert trello board link and remove this comment -->
