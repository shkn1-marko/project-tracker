import enum
from datetime import datetime, timezone

from sqlalchemy import Boolean, Column, DateTime, Enum, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class EntryType(str, enum.Enum):
    right_now = "right_now"
    goal = "goal"
    project = "project"


class Status(str, enum.Enum):
    red = "red"
    yellow = "yellow"
    green = "green"


class Entry(Base):
    __tablename__ = "entries"

    id = Column(Integer, primary_key=True)
    type = Column(Enum(EntryType), nullable=False)
    title = Column(String, nullable=False)
    status = Column(Enum(Status), nullable=True)
    pinned = Column(Boolean, default=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
