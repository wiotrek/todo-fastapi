import strawberry

from schemas.task import TaskType, TaskCreateType
from schemas.user import UserType, UserCreateType
from db.repository.user import create_new_user
from db.repository.task import create_new_task


@strawberry.type
class Mutation:
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
