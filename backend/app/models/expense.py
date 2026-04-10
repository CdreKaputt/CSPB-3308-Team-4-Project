from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, DateTime, Boolean, ForeignKey, Numeric
from datetime import datetime, timezone
from decimal import Decimal
from app.extensions import db

class Expense(db.Model):
    __tablename__ = "expenses"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    trip_id: Mapped[int] = mapped_column(Integer, ForeignKey("trips.id"))
    payer_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    amount: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    is_paid: Mapped[bool] = mapped_column(
        Boolean(name="is_expense_paid"), 
        nullable=False, 
        default=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc)
    )
    
    # trip relationship added to trip.py
    
    # no user relationship added as this would pull in all expense across all 
    # trips a user is a member of

    def __init__(
            self, 
            trip_id: int,
            payer_id: int,
            amount: Decimal,
            description: str,
            is_paid: bool
        ):
        self.trip_id = trip_id
        self.payer_id = payer_id
        self.amount = amount
        self.description = description
        self.is_paid = is_paid
        
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = datetime.now(timezone.utc)
    
    
    def __repr__(self):
        return f"<Expense {self.id}>"