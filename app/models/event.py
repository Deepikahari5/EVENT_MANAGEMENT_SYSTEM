from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database.base import Base


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)

    event_name = Column(String(200), nullable=False)

    description = Column(Text)

    start_date = Column(DateTime, nullable=False)

    end_date = Column(DateTime, nullable=False)

    venue = Column(String(255), nullable=False)

    capacity = Column(Integer, nullable=False)

    status = Column(
        String(50),
        default="Upcoming"
    )

    organizer_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    category_id = Column(
        Integer,
        ForeignKey("categories.id")
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    organizer = relationship("User")

    category = relationship("Category")