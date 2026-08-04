from config.database import Session
from models import Employee, Department


def check_employee(employee_id):
    session = Session()

    try:
        employee = session.get(Employee, employee_id)

        return employee.id if employee else None

    finally:
        session.close()


def add_employee(name, department_name, email):
    session = Session()

    try:
        department = (
            session.query(Department)
            .filter(Department.name == department_name)
            .first()
        )

        if department is None:
            return False

        employee = Employee(
            name=name,
            department_id=department.id,
            email=email
        )

        session.add(employee)
        session.commit()

        return True

    except Exception as e:
        print(e)
        session.rollback()
        return False

    finally:
        session.close()


def view_employees():
    session = Session()

    try:
        employees = (
            session.query(Employee)
            .join(Department)
            .all()
        )

        return [
            (
                employee.id,
                employee.name,
                employee.department.name,
                employee.email
            )
            for employee in employees
        ]

    finally:
        session.close()


def update_employee(employee_id, name, email):
    session = Session()

    try:
        employee = session.get(Employee, employee_id)

        if employee is None:
            return False

        employee.name = name
        employee.email = email

        session.commit()

        return True

    except Exception as e:
        print(e)
        session.rollback()
        return False

    finally:
        session.close()


def change_employee_department(employee_id, department_name):
    session = Session()

    try:
        department = (
            session.query(Department)
            .filter(Department.name == department_name)
            .first()
        )

        if department is None:
            return False

        employee = session.get(Employee, employee_id)

        if employee is None:
            return False

        employee.department_id = department.id

        session.commit()

        return True

    except Exception as e:
        print(e)
        session.rollback()
        return False

    finally:
        session.close()


def delete_employee(employee_id):
    session = Session()

    try:
        employee = session.get(Employee, employee_id)

        if employee is None:
            return False

        session.delete(employee)
        session.commit()

        return True

    except Exception as e:
        print(e)
        session.rollback()
        return False

    finally:
        session.close()