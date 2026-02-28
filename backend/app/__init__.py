from flask import Flask
from .extensions import db, migrate
from .config import config

def create_app(config_name="default")
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    migrate.init_app(app, db)

    from .api.users import bp as users_bp
    app.register_blueprint(users_bp, url_prefix="/api/v1/users")

    return app
