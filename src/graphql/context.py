from functools import cached_property
from strawberry.fastapi import BaseContext

from core.auth import get_current_user
from db.session import SessionLocal
from db.models.user import User


class Context(BaseContext):

    @cached_property
    def user(self) -> User or None:
        if not self.request:
            return None

        db = SessionLocal()
        authorization = self.request.headers.get("Authorization", None)
        return get_current_user(db, authorization)


async def get_context() -> Context:
    return Context()
