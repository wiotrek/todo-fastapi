import strawberry
from strawberry.types import Info
import typing

from src.graphql.auth import IsAuthenticated
from src.db.repository import get_user_list, get_tasks_for_user
from src.schemas import UserType, TaskType


@strawberry.type
class Query:

    @strawberry.field(permission_classes=[IsAuthenticated])
    def all_users(self) -> typing.List[UserType]:
        return get_user_list()

    @strawberry.field(permission_classes=[IsAuthenticated])
    def get_task(self, info: Info) -> typing.List[TaskType]:
        user_id = info.context.user.id
        return get_tasks_for_user(user_id)
