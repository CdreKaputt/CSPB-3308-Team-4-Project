import pytest
from werkzeug.security import generate_password_hash
from app import create_app
from app.extensions import db
from app.models import User


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app("testing")
    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client


@pytest.fixture(scope="module")
def init_database(test_client):
    db.create_all()
    
    default_user = User(
        username="test_user",
        email="testuser@flake.com",
        first_name="Test",
        last_name="User",
        password_digest=generate_password_hash("testpassword"),
    )
    db.session.add(default_user)

    # Add any additional seed data here

    yield
    
    # Teardown
    db.drop_all()


@pytest.fixture(autouse=True)
def clear_session(test_client):
    yield
    with test_client.session_transaction() as session:
        session.clear()


