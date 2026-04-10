import os
from dotenv import load_dotenv
load_dotenv()
import random
from datetime import date, timedelta
from faker import Faker
from app import create_app
from app.extensions import db
from app.models import User, Trip, Events # Only the essentials
from werkzeug.security import generate_password_hash

app = create_app("development")
fake = Faker()

def seed_database():
    with app.app_context():
        print("--- Resetting DB ---")
        db.drop_all()
        db.create_all()
        
        # 1. Create Demo User
        print("--- Generating Demo User ---")
        demo_user = User(
            username="demouser",
            email="demouser@flake.com",
            first_name="Demo",
            last_name="User",
            password_digest=generate_password_hash("password")
        )
        db.session.add(demo_user)
        db.session.commit()
            
        # 2. Create one "Main" Trip for the Demo User
        print("--- Generating Trip ---")
        start = date.today() + timedelta(days=7)
        end = start + timedelta(days=5)
        
        main_trip = Trip(
            trip_name="Estes Park Getaway",
            leader_id=demo_user.id,
            start_date=start,
            end_date=end,
            public=True
        )
        db.session.add(main_trip)
        db.session.commit()
        
        # 3. Generate Events for that Trip
        print("--- Generating Events ---")
        event_options = [
            ("Morning Hike", "Trail ridge road exploration."),
            ("Dinner at The Stanley", "Checking out the haunted hotel."),
            ("White Water Rafting", "Class III rapids on the river."),
            ("Downtown Shopping", "Buying souvenirs and taffy."),
            ("Campfire S'mores", "Relaxing by the fire at the cabin.")
        ]
        
        for name, desc in event_options:
            new_event = Events(
                event_name=name,
                description=desc,
                event_date=main_trip.start_date + timedelta(days=random.randint(0, 4)),
                owner_id=demo_user.id,
                trip_id=main_trip.id
            )
            db.session.add(new_event)
            
        db.session.commit()
        print("--- Seeding Complete! ---")
        print(f"Check your dashboard for Trip ID: {main_trip.id}")

if __name__ == "__main__":
    seed_database()