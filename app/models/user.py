from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String(150), nullable=False)

    email = Column(String(150), unique=True, nullable=False)

    password_hash = Column(String(255), nullable=False)

    role_id = Column(Integer, ForeignKey("roles.id"))

    is_active = Column(Boolean, default=True)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    role = relationship(
        "Role",
        back_populates="users"
    )
    