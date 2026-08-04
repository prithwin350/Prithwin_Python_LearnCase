from config.database import Session
from models import Task, Employee


def check_task(task_id):
    session = Session()

    try:
        task = session.get(Task, task_id)

        return task.id if task else None

    finally:
        session.close()


def add_task(title, description, employee_id):

    session = Session()

    try:
        employee = session.get(Employee, employee_id)

        if employee is None:
            return False

        task = Task(
            title=title,
            description=description,
            status="Pending",
            employee_id=employee_id
        )

        session.add(task)
        session.commit()

        return True

    except Exception as e:
        print(e)
        session.rollback()
        return False

    finally:
        session.close()


def view_tasks():

    session = Session()

    try:
        tasks = (
            session.query(Task)
            .join(Employee)
            .order_by(Task.id.asc())
            .all()
        )

        return [
            (
                task.id,
                task.title,
                task.description,
                task.employee.name,
                task.status
            )
            for task in tasks
        ]

    finally:
        session.close()


def update_task(task_id, field, value):

    session = Session()

    try:
        task = session.get(Task, task_id)

        if task is None:
            return False


        allowed_fields = {
            "title",
            "description",
            "employee_id"
        }

        if field not in allowed_fields:
            return False


        if field == "employee_id":

            employee = session.get(Employee, value)

            if employee is None:
                return False


        setattr(task, field, value)

        session.commit()

        return True


    except Exception as e:
        print(e)
        session.rollback()
        return False

    finally:
        session.close()



def change_task_status(task_id, status):

    session = Session()

    try:
        task = session.get(Task, task_id)

        if task is None:
            return False


        allowed_statuses = {
            "Pending",
            "In Progress",
            "Completed"
        }


        if status not in allowed_statuses:
            return False


        task.status = status

        session.commit()

        return True


    except Exception as e:
        print(e)
        session.rollback()
        return False

    finally:
        session.close()



def delete_task(task_id):

    session = Session()

    try:
        task = session.get(Task, task_id)

        if task is None:
            return False


        session.delete(task)
        session.commit()

        return True


    except Exception as e:
        print(e)
        session.rollback()
        return False

    finally:
        session.close()