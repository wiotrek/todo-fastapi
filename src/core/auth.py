import jwt
from datetime import datetime, timedelta
from sqlalchemy.orm import Session

from core.hashing import Hasher
from db.models.user import User
from db.repository.user import create_new_user
from db.session import SessionLocal
from schemas.token import TokenType
from schemas.user import UserCreateType

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def get_user(username: str):
    db: Session = SessionLocal()
    return db.query(User).filter(User.username == username).first()


def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not Hasher.verify_password(password, user.hashed_password):
        return False
    return user


def register_user(user_create: UserCreateType) -> TokenType:
    user_type = create_new_user(user_create)
    access_token = create_access_token(data={"sub": user_type.username})
    return TokenType(access_token=access_token, token_type="bearer")


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(token: str):
    credentials_exception = Exception("Could not validate credentials")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except jwt.DecodeError:
        raise credentials_exception
    user = get_user(username)
    if user is None:
        raise credentials_exception
    return user
