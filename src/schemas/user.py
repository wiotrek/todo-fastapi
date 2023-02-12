from pydantic import BaseModel


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
