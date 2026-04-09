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
    # Test that members can also access single trip
    response = test_client.get(f"/events/{EVENT_ID}")
    assert response.status_code == 200
    assert b"Test Event" in response.data


def test_events_get_one_as_non_member(test_client, init_database, log_in_non_member_user):
    # Non-memebers should be redirected back to /trips.
    response = test_client.get(f"/events/{EVENT_ID}")
    assert response.status_code == 302  # A 401 might be better
    assert response.headers["Location"] == "/trips" # Double check this


def test_events_get_one_unauthenticated(test_client, init_database):
    response = test_client.get(f"/events/{EVENT_ID}")
    assert response.status_code == 302
    assert response.headers["Location"] == "/login"

# --------------------------------------
# GET /events/new
# --------------------------------------

# --------------------------------------
# POST /events/new
# --------------------------------------

# --------------------------------------
# GET /events/edit/<int:event_id>
# --------------------------------------

# --------------------------------------
# POST /events/edit/<int:event_id>
# --------------------------------------

# --------------------------------------
# POST /events/delete/<int:event_id>
# --------------------------------------