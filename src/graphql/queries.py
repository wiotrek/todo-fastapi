import strawberry
import typing

from src.graphql.auth import IsAuthenticated
from src.db.repository.user import get_user_list
from src.schemas.user import UserType


@strawberry.type
class Query:

    @strawberry.field(permission_classes=[IsAuthenticated])
    def all_users(self) -> typing.List[UserType]:
        return get_user_list()
