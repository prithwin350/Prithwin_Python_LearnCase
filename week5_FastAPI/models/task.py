from datetime import datetime

from sqlalchemy import DateTime
from database.database import Base
from sqlalchemy.orm import Mapped, mapped_column


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    completed: Mapped[bool] = mapped_column(default=False)
    priority: Mapped[int] = mapped_column(default=1)

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )