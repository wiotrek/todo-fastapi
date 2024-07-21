from typing import Optional
from pydantic import BaseModel
from datetime import date, datetime
import strawberry


# shared properties
class TaskBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    date_posted: Optional[date] = datetime.now().date()


# this will be used to validate data while creating a Job
class TaskCreate(TaskBase):
    title: str
    description: str


# this will be used to validate data while creating a Job
class TaskUpdate(BaseModel):
    title: str
    description: str


@strawberry.type
class TaskType(TaskBase):
    owner_id: int
    title: str
    description: Optional[str]

    class Config:  # to convert non dict obj to json
        orm_mode = True
