from db.session import SessionLocal
from src.schemas.user import UserCreateType
from src.db.models.user import User
from src.core.hashing import Hasher
from src.schemas.user import UserType


def create_new_user(user: UserCreateType):
    db = SessionLocal()
    user = User(
        username=user.username,
        hashed_password=Hasher.get_password_hash(user.password),
        discord=user.discord,
        is_active=True,
        is_superuser=False,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return UserType.from_orm(user)


def get_user_list():
    db = SessionLocal()
    users = db.query(User).all()
    return [UserType.from_orm(user) for user in users]
