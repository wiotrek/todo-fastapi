import strawberry
import typing

from src.db.repository.user import get_user_list
from src.schemas.user import UserType
from src.graphql.context import Context


@strawberry.type
class Query:
    @strawberry.field
    def all_users(self, info) -> typing.List[UserType]:
        context: Context = info.context

        if isinstance(context, Context) and context.user:
            return get_user_list()
        raise Exception("Not authenticated")
