# Flake Setup and Running Instructions

This guide provides step-by-step instructions for setting up and runing Flak on
your local development environment.

## 1. Clone this Repository
- cd to where you would like this repo to live on your local machine
  - run `git clone https://github.com/CdreKaputt/CSPB-3308-Team-4-Project.git`
  - cd into your newly cloned copy of `Flake`

## 2. Environment Variables Configuration
- cd into the `backend` directory
- copy the `.env.example` file 
  - `cp .env.example .env`
- open your new `.env` file
  - set up the development db: `DEV_DATABASE_URL=sqlite:///dev.db`
  - set up the secret key: `SECRET_KEY=any-alphanumeric-string`
    - you can generate one yourself
    - or you can run `python3 -c "import secrets; print(secrets.token_hex(32))"` 
      in your browser to generate one
    - NOTE: no quotes around this string are necessary

## 3. Backend Virtual Environment and Requirements
- make sure you are still in the `backend` directory
- create the virtual environment `python -m venv venv`
- active the environment
  - ensure you have execute permissions to active your virtual environment
    - run `chmod +x venv/bin/activate`
  - run `source ./venv/bin/acticate`
- install dependencies
  - run `pip install -r requirements.txt`

## 4. Database Setup
- still in the `backend` directory
  - run `flask db upgrade`

- if you run into any trouble, reset the db migrations as follows
  - delete the `instance` directory 
    - run `rm -rf instance`
  - delete the `migrations` directory 
    - run `rm -rf migrations`
  - ensure no `dev.db` file is floating around your backend
    - run `rm -rf dev.db`
  - re-initialize the db
    - run `flask db init`
  - re-build the migrations
    - run `flask db migrate -m "re-initialize migrations"`
  - upgrade the db
    - `flask db upgrade`

- seed the db
  - run `python seed.py`

## 5. Run the application
- still in the `backend` directory
  - run `flask run`
  - navigate to <a href="http://127.0.0.1:8000">http://127.0.0.1:8000<a>
