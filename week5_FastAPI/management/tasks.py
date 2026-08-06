from database.database import SessionLocal
from models import Task
from schemas import TaskBase


def create_task(task: TaskBase):
    session = SessionLocal()

    try:
        new_task = Task(
            title=task.title,
            description=task.description,
            completed=task.completed,
            priority=task.priority
        )

        session.add(new_task)
        session.commit()
        session.refresh(new_task)

        return new_task

    except Exception as e:
        session.rollback()
        raise e

    finally:
        session.close()


def get_tasks():
    session = SessionLocal()

    try:
        return session.query(Task).all()

    finally:
        session.close()


def get_task(task_id: int):
    session = SessionLocal()

    try:
        return session.get(Task, task_id)

    finally:
        session.close()



def update_task(task_id: int, task: TaskBase):
    session = SessionLocal()

    try:
        existing_task = session.get(Task, task_id)

        if existing_task is None:
            return None

        existing_task.title = task.title
        existing_task.description = task.description
        existing_task.completed = task.completed
        existing_task.priority = task.priority

        session.commit()
        session.refresh(existing_task)

        return existing_task

    except Exception as e:
        session.rollback()
        raise e

    finally:
        session.close()

def delete_task(task_id: int):
    session = SessionLocal()

    try:
        task = session.get(Task, task_id)

        if task is None:
            return False

        session.delete(task)
        session.commit()

        return True

    except Exception as e:
        session.rollback()
        raise e

    finally:
        session.close()