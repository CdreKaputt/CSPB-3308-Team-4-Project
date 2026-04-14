from app.models import Item
from app.extensions import db

TRIP_ID = 1
ITEM_ID = 1  # leader_item, first item created in init_database

# --------------------------------------
# GET /items/<trip_id>  (packlist)
# --------------------------------------

def test_packlist_get_authenticated(test_client, init_database, log_in_default_user):
    response = test_client.get(f"/items/{TRIP_ID}")
    assert response.status_code == 200
    assert b"Test Trip" in response.data
    assert b"Pack List" in response.data
    assert b"Test Items" in response.data  # category present on all seed items


def test_packlist_get_unauthenticated(test_client, init_database):
    response = test_client.get(f"/items/{TRIP_ID}")
    assert response.status_code == 302
    assert response.headers["Location"] == "/login"


# --------------------------------------
# GET /items/new
# --------------------------------------

def test_new_item_get_authenticated(test_client, init_database, log_in_default_user):
    response = test_client.get(f"/items/new?trip_id={TRIP_ID}")
    assert response.status_code == 200
    assert b"<form" in response.data


def test_new_item_get_unauthenticated(test_client, init_database):
    response = test_client.get(f"/items/new?trip_id={TRIP_ID}")
    assert response.status_code == 302
    assert response.headers["Location"] == "/login"


# --------------------------------------
# POST /items/new
# --------------------------------------

def test_new_item_post_authenticated(test_client, init_database, log_in_default_user):
    response = test_client.post(
        "/items/new",
        data={
            "trip_id": TRIP_ID,
            "name": "New Test Item",
            "description": "A newly created test item",
            "category": "Test Category",
            "quantity": 1,
        },
    )
    assert response.status_code == 302

    item = Item.query.filter_by(name="New Test Item").first()
    assert item is not None
    assert item.description == "A newly created test item"
    assert item.trip_id == TRIP_ID


def test_new_item_post_unauthenticated(test_client, init_database):
    response = test_client.post(
        "/items/new",
        data={
            "trip_id": TRIP_ID,
            "name": "Unauthorized Item",
            "description": "Should not be created",
            "category": "Test Category",
            "quantity": 1,
        },
    )
    assert response.status_code == 302
    assert response.headers["Location"] == "/login"

    item = Item.query.filter_by(name="Unauthorized Item").first()
    assert item is None


# --------------------------------------
# GET /items/<item_id>/edit
# --------------------------------------

def test_edit_item_get_authenticated(test_client, init_database, log_in_default_user):
    response = test_client.get(f"/items/{ITEM_ID}/edit")
    assert response.status_code == 200
    assert b"<form" in response.data


def test_edit_item_get_unauthenticated(test_client, init_database):
    response = test_client.get(f"/items/{ITEM_ID}/edit")
    assert response.status_code == 302
    assert response.headers["Location"] == "/login"


# --------------------------------------
# POST /items/<item_id>/edit
# --------------------------------------

def test_edit_item_post_authenticated(test_client, init_database, log_in_default_user):
    response = test_client.post(
        f"/items/{ITEM_ID}/edit",
        data={
            "name": "Updated Item Name",
            "description": "Updated description",
            "category": "Updated Category",
            "quantity": 3,
            "is_completed": "",
        },
    )
    assert response.status_code == 302

    item = db.session.get(Item, ITEM_ID)
    assert item.name == "Updated Item Name"
    assert item.description == "Updated description"
    assert item.quantity == 3


def test_edit_item_post_unauthenticated(test_client, init_database):
    response = test_client.post(
        f"/items/{ITEM_ID}/edit",
        data={
            "name": "Unauthorized Update",
            "description": "Should not be updated",
            "category": "Test Category",
            "quantity": 1,
        },
    )
    assert response.status_code == 302
    assert response.headers["Location"] == "/login"

    item = db.session.get(Item, ITEM_ID)
    assert item.name != "Unauthorized Update"


# --------------------------------------
# POST /items/<item_id>/delete
# --------------------------------------

def test_delete_item_unauthenticated(test_client, init_database):
    response = test_client.post(f"/items/{ITEM_ID}/delete")
    assert response.status_code == 302
    assert response.headers["Location"] == "/login"

    item = db.session.get(Item, ITEM_ID)
    assert item is not None


# Note: authenticated delete test runs last to avoid removing the item
# that other tests depend on.
def test_delete_item_authenticated(test_client, init_database, log_in_default_user):
    response = test_client.post(f"/items/{ITEM_ID}/delete")
    assert response.status_code == 302

    item = db.session.get(Item, ITEM_ID)
    assert item is None
