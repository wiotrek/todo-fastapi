import strawberry
from strawberry.types import Info

from src.graphql.auth import IsAuthenticated
from core.auth import authenticate_user, create_access_token, register_user
from schemas.task import TaskType, TaskCreateType
from schemas.token import TokenType
from schemas.user import UserCreateType
from db.repository.task import create_new_task


@strawberry.type
class Mutation:

    @strawberry.mutation
    def login(self, username: str, password: str) -> TokenType:
        user = authenticate_user(username, password)
        if not user:
            raise Exception("Invalid credentials")
        access_token = create_access_token(data={"sub": user.username})
        return TokenType(access_token=access_token, token_type="bearer")

    @strawberry.mutation
    def register(self, username: str, password: str, discord: str) -> TokenType:
        user_create = UserCreateType(username=username, password=password, discord=discord)
        token_type = register_user(user_create)
        return token_type

    @strawberry.mutation(permission_classes=[IsAuthenticated])
    def create_task(self, info: Info, title: str) -> TaskType:
        task_create = TaskCreateType(
            title=title,
            owner_id=info.context.user.id
        )
        return create_new_task(task_create)
