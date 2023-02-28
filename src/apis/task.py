from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from src.schemas.task import TaskCreate, ShowTask
from src.db.session import get_db
from src.db.repository.task import create_new_task, get_task_list


router = APIRouter()


@router.get("/")
def create_task(db: Session = Depends(get_db)):
    tasks = get_task_list(db)
    return tasks


@router.post("/create-task", response_model=ShowTask)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    current_user = 1
    task = create_new_task(task=task, db=db, owner_id=current_user)
    return task
