from typing import Optional
from pydantic import BaseModel
from datetime import date, datetime


# shared properties
class TaskBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    date_posted: Optional[date] = datetime.now().date()


# this will be used to validate data while creating a Job
class TaskCreate(TaskBase):
    title: str
    description: str


# this will be used to format the response to not to have id,owner_id etc
class ShowTask(TaskBase):
    title: str
    date_posted: date
    description: Optional[str]

    class Config:  # to convert non dict obj to json
        orm_mode = True
