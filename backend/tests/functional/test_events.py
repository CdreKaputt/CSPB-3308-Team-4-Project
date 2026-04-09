from app.models import Event

EVENT_ID = 1

# --------------------------------------
# GET /events/<int:event_id>
# --------------------------------------

def test_events_get_one_as_leader(test_client, init_database, log_in_default_user):
    response = test_client.get(f"/events/{EVENT_ID}")
    assert response.status_code == 200
    assert b"Test Event" in response.data


def test_events_get_one_as_member(test_client, init_database, log_in_member_user):
    # Test that members can also access single event
    response = test_client.get(f"/events/{EVENT_ID}")
    assert response.status_code == 200
    assert b"Test Event" in response.data


def test_events_get_one_as_non_member(test_client, init_database, log_in_non_member_user):
    # Non-memebers should be redirected back to /trips.
    response = test_client.get(f"/events/{EVENT_ID}")
    assert response.status_code == 401  # Possible redirect added later


def test_events_get_one_unauthenticated(test_client, init_database):
    response = test_client.get(f"/events/{EVENT_ID}")
    assert response.status_code == 302
    assert response.headers["Location"] == "/login"

# --------------------------------------
# GET /events/new
# --------------------------------------

def test_events_new_get(test_client, log_in_default_user):
    # Requires active session of any type
    response = test_client.get("/events/new")
    assert response.status_code == 200
    assert b"<form" in response.data


def test_events_new_get_unauthenticated(test_client):
    response = test_client.get("/events/new")
    assert response.status_code == 302
    assert response.headers["Location"] == "/login"

# --------------------------------------
# POST /events/new
# --------------------------------------

def test_events_new_post_valid(test_client, init_database, log_in_default_user):
    response = test_client.post(
        "/events/new",
        data={
            "event_name": "New Test Event",
            "description": "Description of test event",
            "date": "2026-05-07",
        },
    )
    assert response.status_code == 302  # Redirect to new event page or trip page
    
    event = Event.query.filter_by(event_name="New Test Event").first()
    assert event is not None
    assert str(event.description) == "Description of test event"
    assert str(event.date) == "2026-05-07"


def test_events_new_post_valid_as_member(test_client, init_database, log_in_member_user):
    # This assumes memebers can create events
    response = test_client.post(
        "/events/new",
        data={
            "event_name": "New Member Event",
            "description": "Description of member event",
            "date": "2026-05-07",
        },
    )
    assert response.status_code == 302  # Redirect to new event page or trip page
    
    event = Event.query.filter_by(event_name="New Member Event").first()
    assert event is not None
    assert str(event.description) == "Description of member event"
    assert str(event.date) == "2026-05-07"


def test_events_new_post_non_member(test_client, init_database, log_in_member_user):
    # This assumes memebers can create events
    response = test_client.post(
        "/events/new",
        data={
            "event_name": "Non-member Event",
            "description": "Description of non-member event",
            "date": "2026-05-07",
        },
    )
    event = Event.query.filter_by(event_name="Non-member Event").first()
    assert event is None
    assert response.status_code == 401  # Unauthorized 


def test_events_new_post_missing_fields(test_client, init_database, log_in_default_user):
    response = test_client.post(
        "/events/new",
        data={"event_name": "", "description": "", "date": ""},
    )
    # 200 status code expected even though submission was invalid
    # This is standard behavior in Flask
    assert response.status_code == 200
    assert b"required" in response.data.lower()


def test_events_new_post_unauthenticated(test_client):
    response = test_client.post(
        "/events/new",
        data={
            "event_name": "Unathorized Event",
            "description": "Description of unathorized event",
            "date": "2026-05-07",
        },
    )
    event = Event.query.filter_by(event_name="Unathorized Event").first()
    assert event is None
    assert response.status_code == 302
    assert response.headers["Location"] == "/login"

# --------------------------------------
# GET /events/edit/<int:event_id>
# --------------------------------------

def test_events_edit_get_as_leader(test_client, init_database, log_in_default_user):
    response = test_client.get(f"/events/edit/{EVENT_ID}")
    assert response.status_code == 200
    assert b"<form" in response.data


def test_events_edit_get_as_member(test_client, init_database, log_in_member_user):
    # This test assumes that members can edit events
    response = test_client.get(f"/events/edit/{EVENT_ID}")
    assert response.status_code == 200
    assert b"<form" in response.data


def test_events_edit_get_as_non_member(test_client, init_database, log_in_non_member_user):
    response = test_client.get(f"/events/edit/{EVENT_ID}")
    assert response.status_code == 401  # Possible redirect added later


def test_events_edit_get_unauthenticated(test_client, init_database):
    response = test_client.get(f"/events/edit/{EVENT_ID}")
    assert response.status_code == 302
    assert response.headers["Location"] == "/login"

# --------------------------------------
# POST /events/edit/<int:event_id>
# --------------------------------------

# --------------------------------------
# POST /events/delete/<int:event_id>
# --------------------------------------