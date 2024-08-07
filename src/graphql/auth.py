from strawberry.permission import BasePermission
from strawberry.types import Info
import typing

from src.core.auth import get_current_user
from db.session import SessionLocal


class IsAuthenticated(BasePermission):
    message = "User is not authenticated"

    # This method can also be async!
    def has_permission(self, source: typing.Any, info: Info, **kwargs) -> bool:
        request = info.context.request
        db = SessionLocal()

        if "Authorization" in request.headers:
            return get_current_user(db, request.headers["Authorization"])

        return False
