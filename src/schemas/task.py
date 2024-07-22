from typing import Optional
from pydantic import BaseModel
import strawberry


class TaskCreateType(BaseModel):
    owner_id: int
    title: str


@strawberry.type
class TaskType(BaseModel):
    owner_id: int
    title: str
    description: Optional[str]

    class Config:
        orm_mode = True
