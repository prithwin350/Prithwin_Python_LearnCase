from config.database import Session
from models import Department


def check_department(name):
    session = Session()

    try:
        department = (
            session.query(Department)
            .filter(Department.name.ilike(name))
            .first()
        )

        return department.id if department else None

    finally:
        session.close()


def add_department(name):
    session = Session()

    try:
        if check_department(name) is not None:
            return False

        department = Department(
            name=name
        )

        session.add(department)
        session.commit()

        return True

    except Exception as e:
        print(e)
        session.rollback()
        return False

    finally:
        session.close()


def view_departments():
    session = Session()

    try:
        departments = (
            session.query(Department)
            .order_by(Department.id.asc())
            .all()
        )

        return [
            (
                department.id,
                department.name
            )
            for department in departments
        ]

    finally:
        session.close()


def update_department(department_id, name):
    session = Session()

    try:
        department = session.get(
            Department,
            department_id
        )

        if department is None:
            return False

        department.name = name

        session.commit()

        return True

    except Exception as e:
        print(e)
        session.rollback()
        return False

    finally:
        session.close()


def delete_department(department_id):
    session = Session()

    try:
        department = session.get(
            Department,
            department_id
        )

        if department is None:
            return False

        session.delete(department)
        session.commit()

        return True

    except Exception as e:
        print(e)
        session.rollback()
        return False

    finally:
        session.close()