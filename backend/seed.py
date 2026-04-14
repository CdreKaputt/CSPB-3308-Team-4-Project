import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

db_uri = os.getenv("DEV_DATABASE_URL")

import random
from decimal import Decimal
from datetime import date, timedelta
from faker import Faker # Import Faker
from app import create_app
from app.extensions import db
from app.models import User, Trip, Expense, Membership
from werkzeug.security import generate_password_hash

app = create_app("development")

fake = Faker() # used for dummy data

def seed_database():
    with app.app_context():
        print("--- Resetting DB ---")
        db.drop_all()
        db.create_all()
        
        # Add users
        print("--- Generating Users ---")
        users = []
        
        # a demo user for quick login testing
        demo_user = User(
                username="demouser",
                email="demouser@flake.com",
                first_name="Demo",
                last_name="User",
                password_digest=generate_password_hash("password")
            )
        db.session.add(demo_user)
        users.append(demo_user)
        
        # 20 additional users for db seeds
        for _ in range(20):
            u = User(
                username=fake.unique.user_name(),
                email=fake.unique.email(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                password_digest=generate_password_hash("password")
            ) 
            db.session.add(u)
            users.append(u)
        db.session.commit()
            
        # Add trips
        print("--- Generating Trips ---")
        # data for 5 trips
        prefixes = ["Epic", "Annual", "Summer", "Weekend", "The Great"]
        locations = ["Yellowstone", "Tokyo", "Berlin", "Moab", "NYC", "Alps"]
        
        trips = []
        for _ in range(5):
            # trip leader and name
            leader = random.choice(users)
            t_name = f"{random.choice(prefixes)} {random.choice(locations)} Trip"
        
            # randome start and end dates
            start = fake.date_between(start_date='today', end_date='+1y')
            end = start + timedelta(days=random.randint(3, 10))
            
            t = Trip(
                trip_name=t_name,
                leader_id=leader.id,
                start_date=start,
                end_date=end,
                public=random.choice([True, False])
            )
            
            db.session.add(t)
            trips.append(t)
        db.session.commit()
        
        # Add memberships and expenses, one loop instead of two
        print("--- Generating Memberships and Add Expenses ---")
        
        expense_items = [
            "Lunch at the Airport", "Hotel Booking", "Rental Car", 
            "Museum Pass", "Late Night Pizza", "Gas Station Snacks",
            "Tour Guide Tip", "Souvenirs", "Parking Fee"
        ]
        
        for trip in trips:
            # add 5-10 users to each trip
            trip_members = random.sample(users, k=random.randint(5, 10))
            
            # make sure trip leader is in trip members
            trip_leader = db.session.query(User).filter_by(id = trip.leader_id).first()
            if trip_leader not in trip_members:
                trip_members.append(trip_leader)
                
            # add memberships
            for member in trip_members:
                m = Membership(trip_id=trip.id, member_id=member.id)
                db.session.add(m)
            
            # add 3-7 expenses for each trip
            for _ in range(random.randint(3, 7)):
                payer = random.choice(trip_members)
                # generate randome cost amount
                amount = Decimal(str(round(random.uniform(5.00, 300.00), 2)))
                
                e = Expense(
                    trip_id=trip.id,
                    payer_id=payer.id,
                    amount=amount,
                    description=random.choice(expense_items),
                    is_paid=random.choice([True, False])
                )
                db.session.add(e)
                
            db.session.commit()
            
        print("--- Seeding Complete ---")

if __name__ == "__main__":
    seed_database()