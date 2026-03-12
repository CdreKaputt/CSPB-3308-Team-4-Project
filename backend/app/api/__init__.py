from app.api.auth import bp as auth_bp
from app.api.users import bp as users_bp

__all__ = [
    "auth_bp", 
    "users_bp"
]
