from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from src.db import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    discord = Column(String, nullable=False, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    tasks = relationship("Task", back_populates="owner")
