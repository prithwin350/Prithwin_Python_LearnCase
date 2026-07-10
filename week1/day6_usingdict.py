employees = {
    101: {"name": "John", "department": "Sales", "salary": 35000},
    102: {"name": "Alice", "department": "HR", "salary": 42000},
    103: {"name": "Bob", "department": "IT", "salary": 55000},
    104: {"name": "Sarah", "department": "Finance", "salary": 48000},
    105: {"name": "Mike", "department": "Marketing", "salary": 39000},
    106: {"name": "Emma", "department": "Operations", "salary": 46000},
    107: {"name": "David", "department": "IT", "salary": 61000},
    108: {"name": "Sophia", "department": "Sales", "salary": 37000},
    109: {"name": "James", "department": "HR", "salary": 44000},
    110: {"name": "Olivia", "department": "Finance", "salary": 52000},
}


def view_employee_list():
    if not employees:
        print("No employees found.")
        return

    print("\nEmployee List")
    print("-" * 40)

    for employee_id, details in employees.items():
        print(f"ID         : {employee_id}")
        print(f"Name       : {details['name']}")
        print(f"Department : {details['department']}")
        print(f"Salary     : ₹{details['salary']}\n")

def delete_employee():
    while True:
        try:
            employee_id = int(input("Enter employee ID to delete: "))

            if employee_id in employees:
                del employees[employee_id]
                print("Employee deleted successfully.")
                view_employee_list()
                return
            else:
                print("Employee not found.")
        except ValueError:
            print("Please enter a valid employee ID.")
            continue

def add_employee():
    print("\nAdd Employee")
    while True:
        employee_id = int(input("Enter employee ID: "))
        if employee_id in employees:
            print("Employee ID already exists. Please enter a unique ID.")
        else:
            break

    name = input("Enter employee name: ")
    department = input("Enter employee department: ")
    salary = float(input("Enter employee salary: "))

    employees[employee_id] = {
        "name": name,
        "department": department,
        "salary": salary
    }
    print("Employee added successfully.")
    view_employee_list()

def update_employee():
    while True:
        try:
            employee_id = int(input("Enter employee ID to update: "))
            break
        except ValueError:
            print("Please enter a valid employee ID.")

    if employee_id not in employees:
        print("Employee not found.")
        return

    print("1. Update Name")
    print("2. Update Department")
    print("3. Update Salary")

    choice = input("Enter your choice: ")

    if choice == "1":
        employees[employee_id]["name"] = input("Enter new name: ")

    elif choice == "2":
        employees[employee_id]["department"] = input(
            "Enter new department: "
        )

    elif choice == "3":
        while True:
            try:
                employees[employee_id]["salary"] = float(
                    input("Enter new salary: ")
                )
                break
            except ValueError:
                print("Invalid input. Please enter a valid salary.")

    else:
        print("Invalid choice.")
        return

    print("Employee updated successfully.")
    view_employee_list()

def employee_manager():
    while True:
        print("\nEmployee Manager")
        print("1. Add Employee")
        print("2. Update Employee")
        print("3. View Employee List")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()

        elif choice == "2":
            update_employee()

        elif choice == "3":
            view_employee_list()

        elif choice == "4":
            delete_employee()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice.")

def main():
    employee_manager()

main()
