from flask import Flask, render_template
from .extensions import db, migrate, csrf
from .config import config


def create_app(config_name="default"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)

    from .routes import auth_bp, main_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    @app.errorhandler(404)
    def not_found(e):
        return render_template("404.html"), 404

    @app.errorhandler(500)
    def server_error(e):
        return render_template("500.html"), 500

    return app
