from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from config.database import Base


class Department(Base):
    __tablename__ = "departments"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)

    employees: Mapped[list["Employee"]] = relationship(
        back_populates="department"
    )


class Employee(Base):
    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    
    department_id: Mapped[int] = mapped_column(
        ForeignKey("departments.id")
    )

    email: Mapped[str]

    department: Mapped["Department"] = relationship(
        back_populates="employees"
    )

    tasks: Mapped[list["Task"]] = relationship(
        back_populates="employee"
    )


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str | None]

    status: Mapped[str] = mapped_column(
        default="Pending"
    )

    employee_id: Mapped[int] = mapped_column(
        ForeignKey("employees.id")
    )

    employee: Mapped["Employee"] = relationship(
        back_populates="tasks"
    )