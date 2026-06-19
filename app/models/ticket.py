from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database.base import Base


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)

    ticket_number = Column(
        String(100),
        unique=True,
        nullable=False
    )

    registration_id = Column(
        Integer,
        ForeignKey("registrations.id")
    )

    status = Column(
        String(50),
        default="Active"
    )

    issued_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    registration = relationship(
        "Registration"
    )