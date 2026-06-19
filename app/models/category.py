from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

from app.database.base import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String(100),
        unique=True,
        nullable=False
    )

    description = Column(Text)