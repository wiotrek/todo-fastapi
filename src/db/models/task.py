from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from db.session import Base


class Task(Base):
    __tablename__ = "task"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    date_posted = Column(Date)
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="tasks")
