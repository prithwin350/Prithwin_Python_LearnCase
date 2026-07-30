from config.database import get_connection
from management.employee import check_employee


def check_task(task_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id
        FROM tasks
        WHERE id = ?
    """, (task_id,))

    task = cursor.fetchone()

    connection.close()

    return task[0] if task else None


def add_task(title, description, employee_id):

    if check_employee(employee_id) is None:
        return False

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO tasks (
                title,
                description,
                status,
                employee_id
            )
            VALUES (?, ?, ?, ?)
        """, (
            title,
            description,
            "Pending",
            employee_id
        ))

        connection.commit()

        return True

    except Exception:
        connection.rollback()
        return False

    finally:
        connection.close()



def view_tasks():
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                tasks.id,
                tasks.title,
                tasks.description,
                employees.name AS employee,
                tasks.status
            FROM tasks
            JOIN employees
            ON tasks.employee_id = employees.id
            ORDER BY tasks.id ASC
        """)

        return cursor.fetchall()

    finally:
        connection.close()


def update_task(task_id, field, value):

    if check_task(task_id) is None:
        return False

    allowed_fields = {
        "title",
        "description",
        "employee_id"
    }

    if field not in allowed_fields:
        return False

    if field == "employee_id":
        if check_employee(value) is None:
            return False

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(f"""
            UPDATE tasks
            SET {field} = ?
            WHERE id = ?
        """, (value, task_id))

        connection.commit()

        return cursor.rowcount > 0

    except Exception:
        connection.rollback()
        return False

    finally:
        connection.close()


def change_task_status(task_id, status):

    if check_task(task_id) is None:
        return False

    allowed_statuses = {
        "Pending",
        "In Progress",
        "Completed"
    }

    if status not in allowed_statuses:
        return False

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            UPDATE tasks
            SET status = ?
            WHERE id = ?
        """, (status, task_id))

        connection.commit()

        return cursor.rowcount > 0

    except Exception:
        connection.rollback()
        return False

    finally:
        connection.close()


def delete_task(task_id):

    if check_task(task_id) is None:
        return False

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            DELETE FROM tasks
            WHERE id = ?
        """, (task_id,))

        connection.commit()

        return cursor.rowcount > 0

    except Exception:
        connection.rollback()
        return False

    finally:
        connection.close()