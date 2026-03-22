from app.models import User

# --------------------------------------
# Login route tests
# --------------------------------------

def test_login_get(test_client):
    response = test_client.get("/login")
    assert response.status_code == 200
    assert b"<form" in response.data


def test_login_post_valid(test_client, init_database):
    response = test_client.post("/login", data={
        "username": "test_user",
        "password": "testpassword"
    })
    assert response.status_code == 302
    assert response.headers["Location"] == "/dashboard"


def test_login_post_invalid_password(test_client, init_database):
    response = test_client.post("/login", data={
        "username": "test_user",
        "password": "wrongpassword"
    })
    assert response.status_code == 200
    assert b"Invalid username or password" in response.data


def test_login_post_invalid_username(test_client, init_database):
    response = test_client.post("/login", data={
        "username": "nonexistent_user",
        "password": "testpassword"
    })
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

    response = test_client.post("/login", data={
        "username": "test_user",
        "password": "testpassword"
    })
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
    response = test_client.post("/signup", data={
        "username": "new_user",
        "email": "newuser@flake.com",
        "first_name": "New",
        "last_name": "User",
        "password": "testpassword",
        "confirm_password": "testpassword"
    })
    assert response.status_code == 302
    assert response.headers["Location"] == "/login"

    user = User.query.filter_by(username="new_user").first()
    assert user is not None
    assert user.email == "newuser@flake.com"