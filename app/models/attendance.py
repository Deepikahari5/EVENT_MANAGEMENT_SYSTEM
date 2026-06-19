from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy.sql import func

from app.database.base import Base


class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    event_id = Column(
        Integer,
        ForeignKey("events.id")
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    status = Column(
        String(50),
        default="Present"
    )

    attendance_time = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )