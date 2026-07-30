from management.employee import (
    add_employee,
    view_employees,
    update_employee,
    delete_employee,
    change_employee_department,
)

from management.department import (
    add_department,
    view_departments,
    update_department,
    delete_department,
)

from ui.task_menu import TASK_MENU

from utils.helpers import get_input, print_table


# =====================================================
# Department UI
# =====================================================

def add_department_ui():
    name = get_input("Enter department name: ")

    if add_department(name):
        print("\nDepartment added successfully.")
    else:
        print("\nDepartment already exists.")


def view_departments_ui():
    headers = ["ID", "Department"]
    print_table(headers, view_departments())


def update_department_ui():
    department_id = get_input("Enter department ID: ", int)
    name = get_input("Enter new department name: ")

    if update_department(department_id, name):
        print("\nDepartment updated successfully.")
    else:
        print("\nDepartment not found.")


def delete_department_ui():
    department_id = get_input("Enter department ID: ", int)

    if delete_department(department_id):
        print("\nDepartment deleted successfully.")
    else:
        print("\nDepartment not found.")


# =====================================================
# Employee UI
# =====================================================

def add_employee_ui():
    name = get_input("Enter employee name: ")
    department_name = get_input("Enter department name: ")
    email = get_input("Enter email: ")

    if add_employee(name, department_name, email):
        print("\nEmployee added successfully.")
    else:
        print("\nDepartment not found.")


def view_employees_ui():
    headers = ["ID", "Name", "Department", "Email"]
    print_table(headers, view_employees())


def update_employee_ui():
    employee_id = get_input("Enter employee ID: ", int)
    name = get_input("Enter new name: ")
    email = get_input("Enter new email: ")

    if update_employee(employee_id, name, email):
        print("\nEmployee updated successfully.")
    else:
        print("\nEmployee not found.")


def change_department_ui():
    employee_id = get_input("Enter employee ID: ", int)
    department_name = get_input("Enter new department name: ")

    if change_employee_department(employee_id, department_name):
        print("\nEmployee department updated successfully.")
    else:
        print("\nEmployee or department not found.")


def delete_employee_ui():
    employee_id = get_input("Enter employee ID: ", int)

    if delete_employee(employee_id):
        print("\nEmployee deleted successfully.")
    else:
        print("\nEmployee not found.")


# =====================================================
# Menu Definitions
# =====================================================

EMPLOYEE_MENU = {
    "title": "EMPLOYEE MANAGEMENT",
    "exit": "Back",
    "options": {
        "1": ("Add Employee", add_employee_ui),
        "2": ("View Employees", view_employees_ui),
        "3": ("Update Employee", update_employee_ui),
        "4": ("Change Department", change_department_ui),
        "5": ("Delete Employee", delete_employee_ui),
    },
}

DEPARTMENT_MENU = {
    "title": "DEPARTMENT MANAGEMENT",
    "exit": "Back",
    "options": {
        "1": ("Add Department", add_department_ui),
        "2": ("View Departments", view_departments_ui),
        "3": ("Update Department", update_department_ui),
        "4": ("Delete Department", delete_department_ui),
    },
}


MAIN_MENU = {
    "title": "MAIN MENU",
    "exit": "Exit",
    "options": {
        "1": ("Employee Management", lambda: show_menu(EMPLOYEE_MENU)),
        "2": ("Department Management", lambda: show_menu(DEPARTMENT_MENU)),
        "3": ("Task Management", lambda: show_menu(TASK_MENU)),
    },
}


# =====================================================
# Generic Menu
# =====================================================

def show_menu(menu):
    while True:
        print("=" * 40)
        print(menu["title"])
        print("=" * 40)

        for key, (label, _) in menu["options"].items():
            print(f"{key}. {label}")

        print(f"0. {menu['exit']}")

        choice = get_input("Select option: ")

        if choice == "0":
            if menu["exit"] == "Exit":
                print("Goodbye!")
            break

        action = menu["options"].get(choice)

        if action:
            action[1]()
        else:
            print("Invalid option.")


# =====================================================
# Entry Point
# =====================================================

def ui():
    show_menu(MAIN_MENU)