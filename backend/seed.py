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
from app.models import User, Trip, Expense, Membership, Events
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
        prefixes = ["Epic", "Annual", "Summer", "Weekend", "The Great", "Hidden"]
        locations = ["Yellowstone", "Tokyo", "Berlin", "Moab", "NYC", "Alps", "Chamonix"]
        trips = []
        
        # ensure demo user has 3 trips
        for i in range(3):
            start = fake.date_between(start_date='today', end_date='+1y')
            t = Trip(
                trip_name=f"{random.choice(prefixes)} {random.choice(locations)} Expedition",
                leader_id=demo_user.id,
                start_date=start,
                end_date=start + timedelta(days=random.randint(4, 8)),
                public=True
            )
            db.session.add(t)
            trips.append(t)
        
        # add 5 more trips
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
        
        # Add memberships, events and expenses, one loop instead of two
        print("--- Generating Memberships, Events and Add Expenses ---")
        
        expense_items = [
            "Lunch at the Airport", 
            "Hotel Booking", 
            "Rental Car", 
            "Museum Pass", 
            "Late Night Pizza", 
            "Gas Station Snacks",
            "Tour Guide Tip", 
            "Souvenirs", 
            "Parking Fee"
        ]
        
        event_types = [
            "Sightseeing", 
            "Dinner Reservation", 
            "Guided Tour", 
            "Hiking", 
            "Skiing", 
            "Photography Session"
        ]
        
        for trip in trips:
            # add 5-10 users to each trip
            trip_members = random.sample(users, k=random.randint(5, 10))
            
            # make sure trip leader is in trip members
            trip_leader = db.session.query(User).filter_by(id = trip.leader_id).first()
            if trip_leader not in trip_members:
                trip_members.append(trip_leader)
            
            if trip.leader_id == demo_user.id and demo_user not in trip_members:
                trip_members.append(demo_user)
            
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
                
            # add 3-5 events pre trip
            for _ in range(random.randint(3, 5)):
                days_out = random.randint(0, (trip.end_date - trip.start_date).days)
                event_date = trip.start_date + timedelta(days=days_out)
                
                event_name = f"{random.choice(event_types)}"
                
                ev = Events(
                    event_name=event_name,
                    description=f"{event_name} during the {trip.trip_name}",
                    event_date=event_date,
                    owner_id=trip.leader_id,
                    trip_id=trip.id
                )
                db.session.add(ev)
                
            db.session.commit()
            
        print("--- Seeding Complete ---")

if __name__ == "__main__":
    seed_database()