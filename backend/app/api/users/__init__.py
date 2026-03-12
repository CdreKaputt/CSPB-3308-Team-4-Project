from flask import Blueprint

bp = Blueprint("users", __name__)

from app.api.users import routes  # noqa: E402, F401  # 'noqa' suppresses linter error

__all__ = [
    "bp",
]
