# --------------------------------------
# GET /trips
# --------------------------------------

def test_trips_get_all(test_client, init_database, log_in_default_user):
    pass

def test_trips_get_all_unauthenticated(test_client):
    pass


# --------------------------------------
# GET /trips/<int:trip_id>
# --------------------------------------

def test_trips_get_one_as_leader(test_client, init_database, log_in_default_user):
    pass

def test_trips_get_one_as_member(test_client, init_database, log_in_member_user):
    pass

def test_trips_get_one_as_non_member(test_client, init_database, log_in_non_member_user):
    pass

def test_trips_get_one_unauthenticated(test_client, init_database):
    pass


# --------------------------------------
# GET /trips/new
# --------------------------------------

def test_trips_new_get(test_client, log_in_default_user):
    pass

def test_trips_new_get_unauthenticated(test_client):
    pass


# --------------------------------------
# POST /trips/new
# --------------------------------------

def test_trips_new_post_valid(test_client, init_database, log_in_default_user):
    pass

def test_trips_new_post_missing_fields(test_client, init_database, log_in_default_user):
    pass

def test_trips_new_post_unauthenticated(test_client):
    pass


# --------------------------------------
# GET /trips/edit/<int:trip_id>
# --------------------------------------

def test_trips_edit_get_as_leader(test_client, init_database, log_in_default_user):
    pass

def test_trips_edit_get_as_member(test_client, init_database, log_in_member_user):
    pass

def test_trips_edit_get_as_non_member(test_client, init_database, log_in_non_member_user):
    pass

def test_trips_edit_get_unauthenticated(test_client, init_database):
    pass


# --------------------------------------
# POST /trips/edit/<int:trip_id>
# --------------------------------------

def test_trips_edit_post_valid(test_client, init_database, log_in_default_user):
    pass

def test_trips_edit_post_as_member(test_client, init_database, log_in_member_user):
    pass

def test_trips_edit_post_as_non_member(test_client, init_database, log_in_non_member_user):
    pass

def test_trips_edit_post_unauthenticated(test_client, init_database):
    pass


# --------------------------------------
# POST /trips/delete/<int:trip_id>
# --------------------------------------

def test_trips_delete_as_leader(test_client, init_database, log_in_default_user):
    pass

def test_trips_delete_as_member(test_client, init_database, log_in_member_user):
    pass

def test_trips_delete_as_non_member(test_client, init_database, log_in_non_member_user):
    pass

def test_trips_delete_unauthenticated(test_client, init_database):
    pass
