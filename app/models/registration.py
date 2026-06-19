from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import DateTime

from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database.base import Base


class Registration(Base):
    __tablename__ = "registrations"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    event_id = Column(
        Integer,
        ForeignKey("events.id")
    )

    status = Column(
        String(50),
        default="Registered"
    )

    registered_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    user = relationship("User")

    event = relationship("Event")