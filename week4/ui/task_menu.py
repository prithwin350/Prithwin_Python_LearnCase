from management.task import (
    check_task,
    add_task,
    view_tasks,
    update_task,
    change_task_status,
    delete_task
)

from utils.helpers import get_input, print_table


# =====================================================
# Task UI
# =====================================================

def add_task_ui():
    title = get_input("Enter task title: ")
    description = get_input("Enter task description: ")
    employee_id = get_input("Enter employee ID: ", int)

    if add_task(title, description, employee_id):
        print("\nTask added successfully.")
    else:
        print("\nEmployee not found.")


def view_tasks_ui():
    headers = ["ID", "Title", "Description", "Employee", "Status"]
    print_table(headers, view_tasks())


def update_task_ui():

    task_id = get_input("Enter task ID: ", int)

    if check_task(task_id) is None:
        print("\nTask not found.")
        return

    print("\nWhat would you like to update?")
    print("1. Title")
    print("2. Description")
    print("3. Assignee")
    print("0. Back")

    choice = get_input("Select option: ")

    if choice == "1":
        title = get_input("Enter new title: ")

        if update_task(task_id, "title", title):
            print("\nTask title updated successfully.")

    elif choice == "2":
        description = get_input("Enter new description: ")

        if update_task(task_id, "description", description):
            print("\nTask description updated successfully.")

    elif choice == "3":
        employee_id = get_input("Enter new employee ID: ", int)

        if update_task(task_id, "employee_id", employee_id):
            print("\nTask assignee updated successfully.")
        else:
            print("\nEmployee not found.")

    elif choice == "0":
        return

    else:
        print("\nInvalid option.")


def change_task_status_ui():

    task_id = get_input("Enter task ID: ", int)

    if check_task(task_id) is None:
        print("\nTask not found.")
        return

    print("\nSelect new status")
    print("1. Pending")
    print("2. In Progress")
    print("3. Completed")
    print("0. Back")

    choice = get_input("Select option: ")

    if choice == "1":
        status = "Pending"

    elif choice == "2":
        status = "In Progress"

    elif choice == "3":
        status = "Completed"

    elif choice == "0":
        return

    else:
        print("\nInvalid option.")
        return

    if change_task_status(task_id, status):
        print("\nTask status updated successfully.")
    else:
        print("\nTask not found.")


def delete_task_ui():

    task_id = get_input("Enter task ID: ", int)

    if check_task(task_id) is None:
        print("\nTask not found.")
        return

    if delete_task(task_id):
        print("\nTask deleted successfully.")
    else:
        print("\nTask not found.")


# =====================================================
# Menu Definition
# =====================================================

TASK_MENU = {
    "title": "TASK MANAGEMENT",
    "exit": "Back",
    "options": {
        "1": ("Add Task", add_task_ui),
        "2": ("View Tasks", view_tasks_ui),
        "3": ("Update Task", update_task_ui),
        "4": ("Change Task Status", change_task_status_ui),
        "5": ("Delete Task", delete_task_ui),
    },
}