import typing

from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status

from db.session import SessionLocal
from schemas.user import UserCreateType
from db.models.user import User
from core.hashing import Hasher
from schemas.user import UserType


def create_new_user(user_create: UserCreateType) -> UserType:
    db = SessionLocal()
    user = User(
        username=user_create.username,
        hashed_password=Hasher.get_password_hash(user_create.password),
        discord=user_create.discord,
        is_active=True,
        is_superuser=False,
    )

    db.add(user)
    try:
        db.commit()
        db.refresh(user)
        return UserType.from_orm(user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="user already exist"
        )


def get_user_list() -> typing.List[UserType]:
    db = SessionLocal()
    users = db.query(User).all()
    return [UserType.from_orm(user) for user in users]
