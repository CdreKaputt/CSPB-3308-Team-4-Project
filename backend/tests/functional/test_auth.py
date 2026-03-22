from app.models import User

# --------------------------------------
# Login route tests
# --------------------------------------


def test_login_get(test_client):
    response = test_client.get("/login")
    assert response.status_code == 200
    assert b"<form" in response.data


def test_login_post_valid(test_client, init_database):
    response = test_client.post(
        "/login", data={"username": "test_user", "password": "testpassword"}
    )
    assert response.status_code == 302
    assert response.headers["Location"] == "/dashboard"


def test_login_post_invalid_password(test_client, init_database):
    response = test_client.post(
        "/login", data={"username": "test_user", "password": "wrongpassword"}
    )
    assert response.status_code == 200
    assert b"Invalid username or password" in response.data


def test_login_post_invalid_username(test_client, init_database):
    response = test_client.post(
        "/login", data={"username": "nonexistent_user", "password": "testpassword"}
    )
    assert response.status_code == 200
    assert b"Invalid username or password" in response.data


def test_login_get_already_logged_in(test_client):
    with test_client.session_transaction() as session:
        session["user"] = "test_user"

    response = test_client.get("/login")
    assert response.status_code == 302


def test_login_post_already_logged_in(test_client):
    with test_client.session_transaction() as session:
        session["user"] = "test_user"

    response = test_client.post(
        "/login", data={"username": "test_user", "password": "testpassword"}
    )
    assert response.status_code == 302


# --------------------------------------
# Signup route tests
# --------------------------------------


def test_signup_get(test_client):
    response = test_client.get("/signup")
    assert response.status_code == 200
    assert b"<form" in response.data


def test_signup_get_already_logged_in(test_client):
    with test_client.session_transaction() as session:
        session["user"] = "test_user"

    response = test_client.get("/signup")
    assert response.status_code == 302


def test_signup_post_valid(test_client, init_database):
    response = test_client.post(
        "/signup",
        data={
            "username": "new_user1",
            "email": "newuser1@flake.com",
            "first_name": "New",
            "last_name": "User",
            "password": "testpassword",
            "confirm_password": "testpassword",
        },
    )
    assert response.status_code == 302
    assert response.headers["Location"] == "/login"

    user = User.query.filter_by(username="new_user1").first()
    assert user is not None
    assert user.email == "newuser1@flake.com"


def test_signup_post_mismatched_passwords(test_client):
    response = test_client.post(
        "/signup",
        data={
            "username": "new_user2",
            "email": "newuser2@flake.com",
            "first_name": "New",
            "last_name": "User",
            "password": "testpassword",
            "confirm_password": "mismatchpassword",
        },
    )
    assert response.status_code == 200
    assert b"Passwords did not match" in response.data


def test_signup_post_duplicate_username(test_client, init_database):
    response = test_client.post(
        "/signup",
        data={
            "username": "test_user",  # Matches default_user from init_database
            "email": "newuser3@flake.com",
            "first_name": "New",
            "last_name": "User",
            "password": "testpassword",
            "confirm_password": "testpassword",
        },
    )
    assert response.status_code == 200
    assert b"Username already taken" in response.data


def test_signup_post_duplicate_email(test_client, init_database):
    response = test_client.post(
        "/signup",
        data={
            "username": "new_user4",
            "email": "testuser@flake.com",  # Matches default_user
            "first_name": "New",
            "last_name": "User",
            "password": "testpassword",
            "confirm_password": "testpassword",
        },
    )
    assert response.status_code == 200
    assert b"Email already registered" in response.data


# --------------------------------------
# Signup route tests
# --------------------------------------


def test_logout_clears_session(test_client):
    with test_client.session_transaction() as session:
        session["user"] = "test_user"

    response = test_client.post("/logout")
    assert response.status_code == 302

    # fresh session_transaction context required
    with test_client.session_transaction() as session:
        assert "user" not in session


def test_logout_redirects_to_login(test_client):
    with test_client.session_transaction() as session:
        session["user"] = "test_user"

    response = test_client.post("/logout")
    assert response.status_code == 302
    assert response.headers["Location"] == "/login"


def test_logout_when_not_logged_in(test_client):
    response = test_client.post("/logout")
    assert response.status_code == 302
    assert response.headers["Location"] == "/login"
