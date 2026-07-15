import csv
import os

fields = [ "employee_id", "name", "department", "salary" ]


def get_input(message, input_type=str):
    while True:
        try:
            return input_type(input(message))
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")

#if there is no format, this will add the .csv
def normalize_filename(filename):
    if not filename.endswith(".csv"):
        filename += ".csv"

    return filename

#check if file exists
def check_file_exists(filename):
    return os.path.exists(filename)


def add_employee(filename, employee):
    with open(filename, "a", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=fields
        )
        writer.writerow(employee)

    print("Employee added successfully.")


def view_employees(filename):
    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)

        print(f"{'ID':<10} {'Name':<20} {'Department':<20} {'Salary':>12}")
        print("-" * 65)

        for employee in reader:
            print(
                f"{employee['employee_id']:<10} "
                f"{employee['name']:<20} "
                f"{employee['department']:<20} "
                f"{employee['salary']:>12}"
            )


def delete_employee(filename, employee_id):
    remaining_employees = []

    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)

        for employee in reader:
            if employee["employee_id"] != str(employee_id):
                remaining_employees.append(employee)

    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=fields
        )

        writer.writeheader()
        writer.writerows(remaining_employees)

    print("Employee deleted successfully.")
    

def create_csv_file(filename):
    filename = normalize_filename(filename)

    if check_file_exists(filename):
        print("Employee CSV file already exists.")
        return

    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()

    print("Employee CSV file created successfully.")

def get_summary(filename):
    total_employees = 0
    total_salary = 0
    highest_salary = 0
    lowest_salary = None

    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)

        for employee in reader:
            salary = float(employee["salary"])

            total_employees += 1
            total_salary += salary

            if salary > highest_salary:
                highest_salary = salary

            if lowest_salary is None or salary < lowest_salary:
                lowest_salary = salary

    if total_employees == 0:
        print("No employees found.")
        return

    average_salary = total_salary / total_employees

    print("\nEmployee Summary")
    print("-" * 30)
    print(f"Total Employees : {total_employees}")
    print(f"Total Salary    : {total_salary:.2f}")
    print(f"Average Salary  : {average_salary:.2f}")
    print(f"Highest Salary  : {highest_salary:.2f}")
    print(f"Lowest Salary   : {lowest_salary:.2f}")


def get_employee_input():
    employee_id = get_input("Enter employee ID: ").zfill(4)
    name = get_input("Enter employee name: ")
    department = get_input("Enter employee department: ")
    salary = get_input("Enter employee salary: ", float)

    employee = {
        "employee_id": employee_id,
        "name": name,
        "department": department,
        "salary": salary
    }

    return employee


def application():
    while True:
        print("\nWelcome to Employee List Manager")
        print("1. Create CSV File")
        print("2. Add Employee Details")
        print("3. View Employee Details")
        print("4. Delete Employee")
        print("5. View Summary")
        print("6. Exit")

        choice = get_input("Enter your choice: ")

        if choice == "1":
            filename = get_input("Enter CSV filename: ")
            create_csv_file(filename)
            view_employees(filename)

        elif choice == "2":
            filename = get_input("Enter CSV filename: ")
            filename = normalize_filename(filename)

            if not check_file_exists(filename):
                print("Employee CSV file does not exist.")
                continue

            employee = get_employee_input()
            add_employee(filename, employee)
            view_employees(filename)
        elif choice == "3":
            filename = get_input("Enter CSV filename: ")
            filename = normalize_filename(filename)

            if not check_file_exists(filename):
                print("Employee CSV file does not exist.")
                continue
            view_employees(filename)

        elif choice == "4":
            filename = get_input("Enter CSV filename: ")
            filename = normalize_filename(filename)
            if not check_file_exists(filename):
                print("Employee CSV file does not exist.")
                continue

            employee_id = get_input("Enter the employee_id: ")
            delete_employee(filename,employee_id)
            view_employees(filename)
        elif choice == "5":
            filename = get_input("Enter CSV filename: ")
            filename = normalize_filename(filename)

            if not check_file_exists(filename):
                print("Employee CSV file does not exist.")
                continue
            view_employees(filename)
            get_summary(filename)

        elif choice == "6":
            print("Exiting application.")
            break
        else:
            print("Invalid choice.")


def main():
    print("Application running")
    application()


if __name__ == "__main__":
    main()