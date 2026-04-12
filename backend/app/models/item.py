from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Text, Date, DateTime, Boolean, ForeignKey
from datetime import date, datetime, timezone
from app.extensions import db


class Item(db.Model):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(primary_key=True)
    trip_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("trips.id", ondelete="CASCADE"), nullable=False
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text)
    quantity: Mapped[int] = mapped_column(Integer, default=1)
    category: Mapped[str] = mapped_column(String(100))
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"), nullable=False)
    created_by: Mapped[int] = mapped_column(
        Integer, ForeignKey("user.id"), nullable=False
    )
    is_completed: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    status: Mapped[str] = mapped_column(String[20], nullable=False, default="active")
    joined_dt: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )
    left_dt: Mapped[datetime] = mapped_column(DateTime(timezone=True))
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

    def __init__(
            self,
            id: int,
            trip_id: int,
            name: str,
            user_id: int,
            created_by: int,
            description: str,
            category: str,
            quantity: int = 1,
            is_completed: bool = False,
            status: str = "active",
        ):
        self.id = id
        self.id = trip_id
        self.name = name
        self.description = description
        self.quantity = quantity
        self.category = category
        self.user_id = user_id
        self.created_by = created_by
        self.is_completed = is_completed
        self.status = status

    def __repr__(self):
        return f"<Item {self.name}"