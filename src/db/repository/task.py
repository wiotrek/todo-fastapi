from datetime import datetime

from db.session import SessionLocal
from schemas.task import TaskCreateType, TaskType
from db.models.task import Task


def create_new_task(task: TaskCreateType):
    db = SessionLocal()
    task_object = Task(
        owner_id=task.owner_id,
        title=task.title,
        description="",
        date_posted=datetime.now().date()
    )
    db.add(task_object)
    db.commit()
    db.refresh(task_object)
    return task_object


def get_tasks_for_user(user_id: int) -> list[TaskType]:
    db = SessionLocal()
    tasks = db.query(Task).filter(Task.owner_id == user_id).all()
    return [TaskType.from_orm(task) for task in tasks]
