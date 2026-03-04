from flask import Blueprint

bp = Blueprint("auth", __name__)

from app.api.auth import routes  # noqa: E402, F401  # 'noqa' suppresses linter error

__all__ = [
    "bp",
]
