from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Date, DateTime, Boolean, ForeignKey
from datetime import date, datetime, timezone
from app.extensions import db

class Events(db.Model):
    __tablename__ = "events"