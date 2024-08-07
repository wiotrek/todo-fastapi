from pydantic import BaseModel
from typing import List, Optional
import strawberry

from src.schemas.task import TaskType


class UserCreateType(BaseModel):
    username: str
    password: str
    discord: str


@strawberry.type
class UserType(BaseModel):
    id: int
    username: str
    discord: str
    tasks: Optional[List[TaskType]] = []

    class Config:
        orm_mode = True
