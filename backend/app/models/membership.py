from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, DateTime, ForeignKey, UniqueConstraint
from datetime import datetime, timezone
from app.extensions import db

class Membership(db.Model):
    __tablename__ = "memberships"
    
    # Ensure user can only be added to trip once
    __table_args__ = (UniqueConstraint("trip_id", "member_id"),)

    id: Mapped[int] = mapped_column(primary_key=True)
    trip_id: Mapped[int] = mapped_column(Integer, ForeignKey("trips.id"))
    member_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
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
            trip_id: int,
            member_id: int
        ):
        self.trip_id = trip_id
        self.member_id = member_id

        # Set datatime explicitly so it's available before flush or commit
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = datetime.now(timezone.utc)

    
    def __repr__(self):
        return f"<Membership {self.id}>"