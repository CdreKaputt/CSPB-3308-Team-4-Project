from flask import Flask, session, redirect, render_template, url_for
from .extensions import db, migrate, jwt
from .config import config
from flask_wtf.csrf import CSRFProtect


def create_app(config_name="default"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    csrf = CSRFProtect(app)

    from .api import auth_bp, users_bp
    from .routes.main_routes import main_bp
    from .routes.auth_form_routes import auth_forms_bp
    
    # Template Routes
    app.register_blueprint(main_bp, url_prefix='/')
    app.register_blueprint(auth_forms_bp, url_prefix='/')
    # API Routes
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(users_bp, url_prefix="/api/users")
    
    return app
