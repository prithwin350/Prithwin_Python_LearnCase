from fastapi import APIRouter

from schemas import TaskBase, UserCreate, UserLogin
from management import (
    create_task,
    get_tasks,
    get_task,
    update_task,
    delete_task,
    create_user,
    login_user,
    get_current_user,
)
router = APIRouter()

@router.post("/users")
def add_user(user: UserCreate):
    return create_user(user)

@router.post("/login")
def login(user: UserLogin):
    return login_user(user)


@router.get("/profile")
def profile(token: str):
    user = get_current_user(token)

    if user is None:
        return {
            "success": False,
            "message": "Invalid or expired token"
        }

    return {
        "success": True,
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }
    }

@router.post("/tasks")
def add_task(token: str, task: TaskBase):
    user = get_current_user(token)

    if user is None:
        return {
            "success": False,
            "message": "Invalid or expired token"
        }

    return create_task(task)


@router.get("/tasks")
def view_tasks(token: str):
    user = get_current_user(token)

    if user is None:
        return {
            "success": False,
            "message": "Invalid or expired token"
        }

    return get_tasks()


@router.get("/tasks/{task_id}")
def view_task(task_id: int, token: str):
    user = get_current_user(token)

    if user is None:
        return {
            "success": False,
            "message": "Invalid or expired token"
        }

    return get_task(task_id)


@router.put("/tasks/{task_id}")
def edit_task(task_id: int, token: str, task: TaskBase):
    user = get_current_user(token)

    if user is None:
        return {
            "success": False,
            "message": "Invalid or expired token"
        }

    return update_task(task_id, task)


@router.delete("/tasks/{task_id}")
def remove_task(task_id: int, token: str):
    user = get_current_user(token)

    if user is None:
        return {
            "success": False,
            "message": "Invalid or expired token"
        }

    return delete_task(task_id)


