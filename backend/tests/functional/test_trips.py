from app.models import Trip

TRIP_ID = 1


# --------------------------------------
# GET /trips
# --------------------------------------


def test_trips_get_all(test_client, init_database, log_in_default_user):
    # init_database and log_in_default_user arguments ensure that default user 
    # is logged in for this test. These args are not called direclty in this test, 
    # but including them ensures that both fixtures are executed for this test
    # and a default user session is active. 
    
    response = test_client.get("/trips")
    assert response.status_code == 200  # Success
    
    # We should see our test trip title somewhere on /test page
    assert b"Test Trip" in response.data


def test_trips_get_all_unauthenticated(test_client):
    # Note the lack of init_database and log_in_*_user args here.
    # No user session active during this test. Redirect to login expected.
    response = test_client.get("/trips")
    assert response.status_code == 302  # 302 redirect status code expected
    assert response.headers["Location"] == "/login"


# --------------------------------------
# GET /trips/<int:trip_id>
# --------------------------------------


def test_trips_get_one_as_leader(test_client, init_database, log_in_default_user):
    response = test_client.get(f"/trips/{TRIP_ID}")
    assert response.status_code == 200
    assert b"Test Trip" in response.data


def test_trips_get_one_as_member(test_client, init_database, log_in_member_user):
    # Test that members can also access single trip
    response = test_client.get(f"/trips/{TRIP_ID}")
    assert response.status_code == 200
    assert b"Test Trip" in response.data


def test_trips_get_one_as_non_member(test_client, init_database, log_in_non_member_user):
    # Non-memebers should be redirected back to /trips.
    response = test_client.get(f"/tests/{TRIP_ID}")
    assert response.status_code == 302
    assert response.headers["Location"] == "/trips"


def test_trips_get_one_unauthenticated(test_client, init_database):
    response = test_client.get(f"/test/{TRIP_ID}")
    assert response.status_code == 302
    assert response.headers["Location"] == "/login"


# --------------------------------------
# GET /trips/new
# --------------------------------------


def test_trips_new_get(test_client, log_in_default_user):
    # Requires active session of any type
    response = test_client.get("/trips/new")
    assert response.status_code == 200
    assert b"<form" in response.data


def test_trips_new_get_unauthenticated(test_client):
    response = test_client.get("/trips/new")
    assert response.status_code == 302
    assert response.headers["Location"] == "/login"


# --------------------------------------
# POST /trips/new
# --------------------------------------


def test_trips_new_post_valid(test_client, init_database, log_in_default_user):
    response = test_client.post(
        "/trips/new",
        data={
            "trip_name": "New Test Trip",
            "start_date": "2026-05-01",
            "end_date": "2026-05-07",
        },
    )
    assert response.status_code == 302  # Redirect to new trip page
    
    trip = Trip.query.filter_by(trip_name="New Test Trip").first()
    assert trip is not None
    assert str(trip.start_date) == "2026-05-01"
    assert str(trip.end_date) == "2026-05-07"


def test_trips_new_post_missing_fields(test_client, init_database, log_in_default_user):
    response = test_client.post(
        "/trips/new",
        data={"trip_name": "", "start_date": "", "end_date": ""},
    )
    # 200 status code expected even though submission was invalid
    # This is standard behavior in Flask
    assert response.status_code == 200
    assert b"required" in response.data.lower()


def test_trips_new_post_unauthenticated(test_client):
    response = test_client.post(
        "/trips/new",
        data={
            "trip_name": "Unathorized Trip",
            "start_date": "2026-05-01",
            "end_date": "2026-05-07",
        },
    )
    trip = Trip.query.filter_by(trip_name="Unathorized Trip").first()
    assert trip is None
    assert response.status_code == 302
    assert response.headers["Location"] == "/login"


# --------------------------------------
# GET /trips/edit/<int:trip_id>
# --------------------------------------


def test_trips_edit_get_as_leader(test_client, init_database, log_in_default_user):
    response = test_client.get(f"/trips/edit/{TRIP_ID}")
    assert response.status_code == 200
    assert b"<form" in response.data


def test_trips_edit_get_as_member(test_client, init_database, log_in_member_user):
    # This test assumes that members don't have edit permissions of core trip data
    response = test_client.get(f"/trips/edit/{TRIP_ID}")
    assert response.status_code == 302  # Redirect to trip page
    assert response.headers["Location"] == f"/trips/{TRIP_ID}"


def test_trips_edit_get_as_non_member(test_client, init_database, log_in_non_member_user):
    response = test_client.get(f"/trips/edit/{TRIP_ID}")
    assert response.status_code == 302
    assert response.headers["Location"] == "/trips"


def test_trips_edit_get_unauthenticated(test_client, init_database):
    response = test_client.get(f"/trips/edit/{TRIP_ID}")
    assert response.status_code == 302
    assert response.headers["Location"] == "/login"


# --------------------------------------
# POST /trips/edit/<int:trip_id>
# --------------------------------------


def test_trips_edit_post_valid(test_client, init_database, log_in_default_user):
    response = test_client.post(
        f"/trips/edit/{TRIP_ID}",
        data={
            "trip_name": "Updated Trip",
            "start_date": "2026-04-01",
            "end_date": "2026-04-10",
        },
    )
    assert response.status_code == 302

    trip = Trip.query.get(TRIP_ID)
    assert trip.trip_name == "Updated Trip"
    assert str(trip.end_date) == "2026-04-10"


def test_trips_edit_post_as_member(test_client, init_database, log_in_member_user):
    # This test assumes that members don't have edit permissions of core trip data
    response = test_client.post(
        f"/trips/edit/{TRIP_ID}",
        data={
            "trip_name": "Member Edit Attempt",
            "start_date": "2026-04-01",
            "end_date": "2026-04-07",
        },
    )
    assert response.status_code == 302
    assert response.headers["Location"] == f"/trips/{TRIP_ID}"


def test_trips_edit_post_as_non_member(test_client, init_database, log_in_non_member_user):
    response = test_client.post(
        f"/trips/edit/{TRIP_ID}",
        data={
            "trip_name": "Non-member Edit Attempt",
            "start_date": "2026-04-01",
            "end_date": "2026-04-07",
        },
    )
    assert response.status_code == 302
    assert response.headers["Location"] == "/trips"


def test_trips_edit_post_unauthenticated(test_client, init_database):
    response = test_client.post(
        f"/trips/edit/{TRIP_ID}",
        data={
            "trip_name": "Unauth Edit Attempt",
            "start_date": "2026-04-01",
            "end_date": "2026-04-07",
        },
    )
    assert response.status_code == 302
    assert response.headers["Location"] == "/login"


# --------------------------------------
# POST /trips/delete/<int:trip_id>
# --------------------------------------
# Note: delete_as_leader runs last to preserve the trip for other delete tests


def test_trips_delete_as_non_member(test_client, init_database, log_in_non_member_user):
    response = test_client.post(f"/trips/delete/{TRIP_ID}")
    assert response.status_code == 302
    assert response.headers["Location"] == "/trips"

    trip = Trip.query.get(TRIP_ID)
    assert trip is not None


def test_trips_delete_as_member(test_client, init_database, log_in_member_user):
    response = test_client.post(f"/trips/delete/{TRIP_ID}")
    assert response.status_code == 302
    assert response.headers["Location"] == f"/trips/{TRIP_ID}"

    trip = Trip.query.get(TRIP_ID)
    assert trip is not None


def test_trips_delete_unauthenticated(test_client, init_database):
    response = test_client.post(f"/trips/delete/{TRIP_ID}")
    assert response.status_code == 302
    assert response.headers["Location"] == "/login"

    trip = Trip.query.get(TRIP_ID)
    assert trip is not None


def test_trips_delete_as_leader(test_client, init_database, log_in_default_user):
    response = test_client.post(f"/trips/delete/{TRIP_ID}")
    assert response.status_code == 302
    assert response.headers["Location"] == "/trips"

    trip = Trip.query.get(TRIP_ID)
    assert trip is None
