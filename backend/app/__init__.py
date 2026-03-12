from flask import Flask
from .extensions import db, migrate, jwt
from .config import config
from flask_cors import CORS


def create_app(config_name="default"):
    app = Flask(__name__)
    CORS(app, supports_credentials=True) # added so react frontend can talk to flask backend
    app.config.from_object(config[config_name])

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    from .api import auth_bp, users_bp

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(users_bp, url_prefix="/api/users")

    return app
