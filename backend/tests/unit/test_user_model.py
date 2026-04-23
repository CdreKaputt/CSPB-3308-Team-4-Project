from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User


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