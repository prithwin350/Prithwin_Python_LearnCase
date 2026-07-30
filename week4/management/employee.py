from config.database import get_connection
from management.department import check_department


def check_employee(employee_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id
        FROM employees
        WHERE id = ?
    """, (employee_id,))

    employee = cursor.fetchone()

    connection.close()

    return employee[0] if employee else None


def add_employee(name, department_name, email):

    department_id = check_department(department_name)

    if department_id is None:
        return False

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO employees (name, department_id, email)
        VALUES (?, ?, ?)
    """, (name, department_id, email))

    connection.commit()
    connection.close()

    return True


def view_employees():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    SELECT
        employees.id,
        employees.name,
        departments.name AS department,
        employees.email
    FROM employees
    JOIN departments
    ON employees.department_id = departments.id
    ORDER BY employees.id ASC
    """)

    employees = cursor.fetchall()

    connection.close()

    return employees


def update_employee(employee_id, name, email):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE employees
        SET name = ?,
            email = ?
        WHERE id = ?
    """, (name, email, employee_id))

    connection.commit()

    updated = cursor.rowcount > 0

    connection.close()

    return updated


def change_employee_department(employee_id, department_name):

    department_id = check_department(department_name)

    if department_id is None:
        return False

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE employees
        SET department_id = ?
        WHERE id = ?
    """, (department_id, employee_id))

    connection.commit()

    updated = cursor.rowcount > 0

    connection.close()

    return updated


def delete_employee(employee_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM employees
        WHERE id = ?
    """, (employee_id,))

    connection.commit()

    deleted = cursor.rowcount > 0

    connection.close()

    return deleted


