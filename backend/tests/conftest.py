import pytest
from datetime import date
from werkzeug.security import generate_password_hash
from app import create_app
from app.extensions import db
from app.models import User, Trip, Membership, Events, Item


@pytest.fixture(scope="module")
def test_client():
    flask_app = create_app("testing")
    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client


@pytest.fixture(autouse=True)
def clear_session(test_client):
    yield
    with test_client.session_transaction() as session:
        session.clear()


@pytest.fixture(scope="module")
def init_database(test_client):
    db.create_all()

    # Create Test Users
    default_user = User(
        username="test_user",
        email="testuser@flake.com",
        first_name="Test",
        last_name="User",
        password_digest=generate_password_hash("testpassword"),
    )
    member_user = User(
        username="member_user",
        email="memberuser@flake.com",
        first_name="Member",
        last_name="User",
        password_digest=generate_password_hash("testpassword"),
    )
    non_member_user = User(
        username="non_member_user",
        email="nonmemberuser@flake.com",
        first_name="Test",
        last_name="User",
        password_digest=generate_password_hash("testpassword"),
    )
    db.session.add(default_user)
    db.session.add(member_user)
    db.session.add(non_member_user)
    db.session.flush()

    # Create Test Trip
    trip = Trip(
        trip_name="Test Trip", 
        leader_id=1, # Default User
        start_date=date(2026, 4, 1),
        end_date=date(2026, 4, 7)
    )
    db.session.add(trip)
    db.session.flush()

    # Create Test Membership between "trip" and "member_user"
    membership = Membership(trip_id=trip.id, member_id=member_user.id)
    db.session.add(membership)

    # Create Test Event
    leader_event = Events(
        event_name="Test Event",
        description="Test event description",
        event_date=date(2026, 4, 4),
        owner_id=default_user.id,
        trip_id=trip.id,
    )
    member_event = Events(
        event_name="Test Event for Member",
        description="Test event for member description",
        event_date=date(2026, 4, 5),
        owner_id=member_user.id,
        trip_id=trip.id,
    )
    db.session.add(leader_event)
    db.session.add(member_event)

    # Create Test Item
    leader_item = Item(
        trip_id=trip.id,
        name="Leader's Test Item",
        user_id=default_user.id,
        created_by=default_user.id,
        description="Item added to list by trip leader",
        category="Test Items",
        # Use default for quantity, is_complete, and status
    )
    member_item = Item(
        trip_id=trip.id,
        name="Memeber's Test Item",
        user_id=member_user.id,
        created_by=member_user.id,
        description="Item added to list by trip member",
        category="Test Items",
    )
    shared_item = Item(
        trip_id=trip.id,
        name="Shared Test Item",
        user_id=member_user.id,
        created_by=default_user.id,
        description="Item added by trip leader but assigned to member",
        category="Test Items",
    )
    db.session.add(leader_item)
    db.session.add(member_item)
    db.session.add(shared_item)
    
    db.session.commit()

    # Add any additional seed data here

    yield

    # Teardown
    db.drop_all()


@pytest.fixture
def log_in_default_user(test_client, init_database):
    with test_client.session_transaction() as session:
        session["user"] = "test_user"
    # No need to run session.clear(). 
    # clear_session already does that. 


@pytest.fixture
def log_in_member_user(test_client, init_database):
    with test_client.session_transaction() as session:
        session["user"] = "member_user"


@pytest.fixture
def log_in_non_member_user(test_client, init_database):
    with test_client.session_transaction() as session:
        session["user"] = "non_member_user"