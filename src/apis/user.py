from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from src.schemas.user import UserCreate, ShowUser
from src.db.session import get_db
from src.db.repository.user import create_new_user, get_user_list

router = APIRouter()


@router.get("/")
def get_users(db: Session = Depends(get_db)):
    users = get_user_list(db)
    return users


@router.get("/{user_id}")
def show_user(user: UserCreate, db: Session = Depends(get_db)):
    return {}


@router.post("/", response_model=ShowUser)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = create_new_user(user=user, db=db)
    return user
