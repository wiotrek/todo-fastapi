from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from src.schemas.user import UserCreate
from src.db.session import get_db
from src.db.repository.user import create_new_user

router = APIRouter()


@router.get("/{user_id}")
def show_user(user_id: int, db: Session = Depends(get_db)):
    return {}


@router.post("/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = create_new_user(user=user, db=db)
    return user

