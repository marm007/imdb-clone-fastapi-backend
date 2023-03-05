from sqlalchemy import VARCHAR, Boolean, Column, DateTime, Integer

from ..database import Base


class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(VARCHAR(150), unique=True, index=True)
    uid = Column(VARCHAR(150), unique=True, index=True)
    birthday = Column(DateTime)
    is_active = Column(Boolean, default=True)
    confirmed_at = Column(DateTime, nullable=True)
