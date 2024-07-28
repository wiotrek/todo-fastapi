import strawberry
from sqlalchemy.orm import Session

from db.session import SessionLocal
from db.models.user import User
from core.auth import get_password_hash, authenticate_user, create_access_token
from schemas.task import TaskType, TaskCreateType
from schemas.token import TokenType
from schemas.user import UserType, UserCreateType
from db.repository.user import create_new_user
from db.repository.task import create_new_task


@strawberry.type
class Mutation:

    @strawberry.mutation
    def register(self, info, user: UserCreateType) -> UserType:
        db: Session = SessionLocal()
        db_user = User(name=user.username, hashed_password=get_password_hash(user.password))
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return UserType(id=db_user.id, name=db_user.name, tasks=[])

    @strawberry.mutation
    def login(self, info, username: str, password: str) -> TokenType:
        db: Session = SessionLocal()
        user = authenticate_user(db, username, password)
        if not user:
            raise Exception("Invalid credentials")
        access_token = create_access_token(data={"sub": user.name})
        return TokenType(access_token=access_token, token_type="bearer")

    @strawberry.mutation
    def create_user(self, username: str, password: str, discord: str) -> UserType:
        user_create = UserCreateType(
            username=username,
            password=password,
            discord=discord
        )
        return create_new_user(user_create)

    @strawberry.mutation
    def create_task(self, owner_id: int, title: str) -> TaskType:
        task_create = TaskCreateType(
            title=title,
            owner_id=owner_id
        )
        return create_new_task(task_create)
