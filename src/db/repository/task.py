from sqlalchemy.orm import Session

from schemas.task import TaskCreate
from db.models.task import Task


def create_new_task(task: TaskCreate, db: Session, owner_id: int):
    task_object = Task(**task.dict(), owner_id=owner_id)
    db.add(task_object)
    db.commit()
    db.refresh(task_object)
    return task_object
