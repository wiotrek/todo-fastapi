from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from src.schemas.task import TaskCreate, ShowTask
from src.db.session import get_db
from src.db.repository.task import create_new_task


router = APIRouter()


@router.post("/create-task", response_model=ShowTask)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    current_user = 1
    task = create_new_task(task=task, db=db, owner_id=current_user)
    return task
