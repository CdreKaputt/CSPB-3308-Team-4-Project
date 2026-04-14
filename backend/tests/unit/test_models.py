from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date
from app.models import User, Trip, Membership, Item


def test_new_user():
    user = User(
        username="test_user",
        email="testuser@flake.com",
        first_name="Test",
        last_name="User",
        password_digest=generate_password_hash("testpassword"),
    )
    assert user.username == "test_user"
    assert user.email == "testuser@flake.com"
    assert user.first_name == "Test"
    assert user.last_name == "User"
    assert check_password_hash(user.password_digest, "testpassword") 
    assert user.password_digest != "testpassword"
    assert user.__repr__() == "<User test_user>"


def test_new_trip():
    trip = Trip(
        trip_name="Test Trip 2026",
        leader_id=1,
        start_date=date(2026, 4, 1),
        end_date=date(2026, 4, 7),
        public=False,
    )
    assert trip.trip_name == "Test Trip 2026"
    assert trip.leader_id == 1
    assert trip.start_date == date(2026, 4, 1)
    assert trip.end_date == date(2026, 4, 7)
    assert trip.__repr__() == "<Trip Test Trip 2026>"


def test_new_membership():
    membership = Membership(
        trip_id=1,
        member_id=1,
    )
    assert membership.trip_id == 1
    assert membership.member_id == 1
    assert membership.__repr__() == f"<Membership {membership.id}>"


def test_new_item():
    item = Item(
        trip_id=1,
        name="Test Item",
        user_id=1,
        created_by=1,
        description="A test item description",
        category="Test Category",
        quantity=2,
    )
    assert item.trip_id == 1
    assert item.name == "Test Item"
    assert item.user_id == 1
    assert item.created_by == 1
    assert item.description == "A test item description"
    assert item.category == "Test Category"
    assert item.quantity == 2
    assert item.is_completed == False
    assert item.status == "active"
    assert item.__repr__() == "<Item: Test Item"


def test_new_item_defaults():
    item = Item(
        trip_id=1,
        name="Minimal Item",
        user_id=1,
        created_by=1,
    )
    assert item.quantity == 1
    assert item.is_completed == False
    assert item.status == "active"
    assert item.description is None
    assert item.category is None