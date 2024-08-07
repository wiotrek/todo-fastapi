import strawberry
from sqlalchemy.orm import Session

from db.session import SessionLocal
from core.auth import authenticate_user, create_access_token, register_user
from schemas.task import TaskType, TaskCreateType
from schemas.token import TokenType
from schemas.user import UserCreateType
from db.repository.task import create_new_task


@strawberry.type
class Mutation:

    @strawberry.mutation
    def login(self, info, username: str, password: str) -> TokenType:
        db: Session = SessionLocal()
        user = authenticate_user(db, username, password)
        if not user:
            raise Exception("Invalid credentials")
        access_token = create_access_token(data={"sub": user.username})
        return TokenType(access_token=access_token, token_type="bearer")

    @strawberry.mutation
    def register(self, username: str, password: str, discord: str) -> TokenType:
        user_create = UserCreateType(username=username, password=password, discord=discord)
        token_type = register_user(user_create)
        return token_type

    @strawberry.mutation
    def create_task(self, owner_id: int, title: str) -> TaskType:
        task_create = TaskCreateType(
            title=title,
            owner_id=owner_id
        )
        return create_new_task(task_create)
