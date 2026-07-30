from config.database import get_connection

def check_department(name):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id
        FROM departments
        WHERE LOWER(name) = LOWER(?)
    """, (name,))

    department = cursor.fetchone()

    connection.close()

    if department:
        return department[0]

    return None


def add_department(name):
    if check_department(name) is not None:
        return False

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO departments (name)
        VALUES (?)
    """, (name,))

    connection.commit()
    connection.close()

    return True


def view_departments():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM departments
        ORDER BY id ASC
    """)

    departments = cursor.fetchall()

    connection.close()

    return departments


def update_department(department_id, name):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE departments
        SET name = ?
        WHERE id = ?
    """, (name, department_id))

    connection.commit()

    updated = cursor.rowcount > 0

    connection.close()

    return updated


def delete_department(department_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM departments
        WHERE id = ?
    """, (department_id,))

    connection.commit()

    deleted = cursor.rowcount > 0

    connection.close()

    return deleted