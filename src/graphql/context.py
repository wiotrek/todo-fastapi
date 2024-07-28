import strawberry

from core.auth import get_current_user
from sqlalchemy.orm import Session
from db.session import SessionLocal
from db.models.user import User


@strawberry.type
class Context:
    user: User
    db: Session


def get_context(token: str = None):
    db = SessionLocal()
    user = None
    if token:
        user = get_current_user(db, token)
    return Context(user=user, db=db)
