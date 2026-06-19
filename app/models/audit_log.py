from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.sql import func

from app.database.base import Base


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(Integer)

    action = Column(
        String(100)
    )

    entity = Column(
        String(100)
    )

    description = Column(
        String(500)
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )