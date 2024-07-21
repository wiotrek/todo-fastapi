from sqlalchemy.orm import Session

from src.schemas.user import UserCreate
from src.db.models.user import User
from src.core.hashing import Hasher
from src.schemas.user import UserType
from src.db.session import SessionLocal


def create_new_user(user: UserCreate, db: Session):
    user = User(
        username=user.username,
        hashed_password=Hasher.get_password_hash(user.password),
        discord="user#123",
        is_active=True,
        is_superuser=False,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_list():
    db = SessionLocal()
    users = db.query(User).all()
    return [UserType.from_orm(user) for user in users]
