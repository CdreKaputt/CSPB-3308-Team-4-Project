from datetime import datetime, timezone
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime
from app.extensions import db


class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(
        String(80), nullable=False, unique=True, index=True
    )
    email: Mapped[str] = mapped_column(
        String(100), nullable=False, unique=True, index=True
    )
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    password_digest: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    # Explicit __init__ makes parameters visible to code editors.
    # SQLAlchemy generates one dynamically but type checkers can't see it.
    def __init__(
        self,
        username: str,
        email: str,
        first_name: str,
        last_name: str,
        password_digest: str,
    ):
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password_digest = password_digest

        # Set datatime explicitly so it's available before flush or commit
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = datetime.now(timezone.utc)

    def __repr__(self):
        return f"<User {self.username}>"
