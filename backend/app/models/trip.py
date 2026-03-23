from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Date, DateTime, Boolean, ForeignKey
from datetime import date, datetime, timezone
from app.extensions import db

class Trip(db.Model):
    __tablename__ = "trips"

    id: Mapped[int] = mapped_column(primary_key=True)
    trip_name: Mapped[str] = mapped_column(String(255), nullable=False)
    leader_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    start_date: Mapped[date] = mapped_column(Date, nullable=False)
    end_date: Mapped[date] = mapped_column(Date, nullable=False)
    public: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
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


    # Possibly add relationship to leader
    # leader: Mapped["User"] = relationship("User", foreign_keys=[leader_id])


    def __init__(
        self,
        trip_name: str,
        leader_id: int,
        start_date: date,
        end_date: date,
        public: bool = False,
    ): 
        self.trip_name = trip_name
        self.leader_id = leader_id
        self.start_date = start_date
        self.end_date = end_date
        self.public = public

        # Set datatime explicitly so it's available before flush or commit
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = datetime.now(timezone.utc)

    
    def __repr__(self):
        return f"<Trip {self.trip_name}>"