from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class TaskBase(BaseModel):
    title: str
    description: str
    completed: bool = False
    priority: int = 1