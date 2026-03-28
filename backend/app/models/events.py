from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Date, DateTime, Boolean, ForeignKey
from datetime import date, datetime, timezone
from app.extensions import db

class Events(db.Model):
    __tablename__ = "events"
    id: Mapped[int] = mapped_column(primary_key=True)
    event_name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    event_date: Mapped[date] = mapped_column(Date, nullable=False)
    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    trip_id: Mapped[int] = mapped_column(Integer, ForeignKey("trips.id"))
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
        event_name: str,
        description: str,
        event_date: date,
        owner_id: int,
        trip_id: int,
    ): 
        self.event_name = event_name
        self.description = description
        self.event_date = event_date
        self.owner_id = owner_id
        self.trip_id = trip_id

        now = datetime.now(timezone.utc)
        self.created_at = now
        self.updated_at = now

    
    def __repr__(self):
        return f"<Event {self.event_name}>"