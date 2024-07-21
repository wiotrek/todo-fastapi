import strawberry
import typing

from src.db.repository.user import get_user_list
from src.schemas.user import UserType


@strawberry.type
class Query:

    all_users: typing.List[UserType] = strawberry.field(resolver=get_user_list)
