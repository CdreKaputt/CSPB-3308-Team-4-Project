from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, DateTime, ForeignKey
from datetime import date, datetime, timezone
from app.extensions import db

class Attendee(db.Model):
    __tablename__ = "attendee"
    id: Mapped[int] = mapped_column(primary_key=True)
    event_id: Mapped[int] = mapped_column(Integer, ForeignKey("events.id"))
    trip_id: Mapped[int] = mapped_column(Integer, ForeignKey("trips.id"))
    attendee_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc)
    )

    def __init__(
        self,
        id: int,
        event_id: int,
        trip_id: int,
        attendee_id: int,
    ): 
        self.id = id
        self.event_id = event_id
        self.trip_id = trip_id
        self.attendee_id = attendee_id

        now = datetime.now(timezone.utc)
        self.created_at = now
        self.updated_at = now

    
    def __repr__(self):
        return f"<Attendee {self.id}>"