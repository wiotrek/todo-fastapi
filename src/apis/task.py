from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from src.schemas.task import TaskCreate, ShowTask, TaskUpdate
from src.db.session import get_db
from src.db.repository.task import (
    create_new_task,
    get_task_single,
    get_task_list,
    edit_task_single,
    remove_task
)


router = APIRouter()


@router.get("/")
def get_tasks(db: Session = Depends(get_db)):
    tasks = get_task_list(db)
    return tasks


@router.get("/{task_id}")
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = get_task_single(task_id=task_id, db=db)
    return task


@router.put("/{task_id}")
def edit_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    current_user = 1
    task = edit_task_single(task=task, task_id=task_id, db=db, owner_id=current_user)
    return task


@router.post("/create-task", response_model=ShowTask)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    current_user = 1
    task = create_new_task(task=task, db=db, owner_id=current_user)
    return task


@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    _ = remove_task(task_id=task_id, db=db)
    return {
        "msg": "removing"
    }
