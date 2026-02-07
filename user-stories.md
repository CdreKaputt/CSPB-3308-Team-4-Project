# User Stories - Team 4

## Story 2:
As a developer, I want to read configuration values from a Python config file so that environment-specific settings are easy to change.

## Story 8:
As a developer, I want to write SQL queries to retrieve filtered records from a database so that users can view only relevant data.

## Story 14:
As a team member, I want to create basic unit tests in Python so that I can verify core functionality before deployment.
 
---

***Here's a typical output (to give you a sense of scale of how much to write):***


## User Story

As a user, I want the script to skip downloads if the file already exists so that time is saved.

*Effort Level*
3

*Acceptance Criteria*

Given the correct year and game ID directory already exists \
When the HTML file is already present \
Then the script does not download the file again \
And the script prints “file already exists, skipping download” 


Given the file does not exist \
When the script runs \
Then the file is downloaded successfully \
And the file appears in the correct directory 

Given the download fails \
When the script attempts the download \
Then an error message is printed \
And the script exits with a non-zero status code 
