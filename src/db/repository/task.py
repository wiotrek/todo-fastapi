from sqlalchemy.orm import Session

from schemas.task import TaskCreate, TaskUpdate
from db.models.task import Task


def create_new_task(task: TaskCreate, db: Session, owner_id: int):
    task_object = Task(**task.dict(), owner_id=owner_id)
    db.add(task_object)
    db.commit()
    db.refresh(task_object)
    return task_object


def get_task_list(db: Session):
    tasks = db.query(Task).all()
    return tasks


def get_task_single(task_id: int, db: Session):
    task = db.query(Task)\
        .filter(Task.id == task_id)\
        .one_or_none()
    return task


def edit_task_single(task_id: int, task: TaskUpdate, db: Session, owner_id: int):
    existing_task = db.query(task).filter(Task.id == task_id)
    if not existing_task.first():
        return 0
    task.__dict__.update(owner_id=owner_id)  # update dictionary with new key value of owner_id
    existing_task.update(task.__dict__)
    db.commit()
    return task
