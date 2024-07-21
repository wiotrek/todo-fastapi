from pydantic import BaseModel
from typing import List, Optional
import strawberry

from src.schemas.task import TaskType


# properties required during user creation
class UserCreate(BaseModel):
    username: str
    password: str
    discord: str


class ShowUser(BaseModel):
    username: str
    is_active: bool

    class Config:
        orm_mode = True


@strawberry.type
class UserType(BaseModel):
    id: int
    username: str
    discord: str
    tasks: Optional[List[TaskType]] = []

    class Config:
        orm_mode = True
