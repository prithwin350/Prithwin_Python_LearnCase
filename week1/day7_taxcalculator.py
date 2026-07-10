def calculate_tax(salary,tax):
    tax_amount = salary * tax / 100
    return tax_amount

def calculate_take_home_salary(salary, tax_amount):
    return salary - tax_amount

def display_menu():
    print("\n========== Tax Calculator ==========")
    print("1. Calculate Tax")
    print("2. Calculate Take Home Salary")
    print("3. Display Salary Summary")
    print("4. Exit")
    print("====================================")


def calculator():
    while True:
        display_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                salary = float(input("Enter salary: "))
                tax = float(input("Enter tax percentage: "))
            except ValueError:
                print("Invalid input. Please enter numeric values only.")
                continue
            tax_amount = calculate_tax(salary,tax)
            print(f"Tax Amount: {tax_amount}")

        elif choice == "2":
            try:
                salary = float(input("Enter salary: "))
                tax = float(input("Enter tax percentage: "))
            except ValueError:
                print("Invalid input. Please enter numeric values only.")
                continue
            tax_amount = calculate_tax(salary, tax)
            take_home_salary = calculate_take_home_salary(salary, tax_amount)
            print(f"Take Home Salary: {take_home_salary}")

        elif choice == "3":
            try:
                salary = float(input("Enter salary: "))
                tax = float(input("Enter tax percentage: "))
            except ValueError:
                print("Invalid input. Please enter numeric values only.")
                continue
            tax_amount = calculate_tax(salary, tax)
            take_home_salary = calculate_take_home_salary(salary, tax_amount)
            print(f"Salary: {salary}")
            print(f"Tax Amount: {tax_amount}")
            print(f"Take Home Salary: {take_home_salary}")

        elif choice == "4":
            print("Thank you for using the Tax Calculator!")
            break

        else:
            print("Invalid choice. Please try again.")

def main():
    print("Welcome to the Tax Calculator!")
    calculator()

main()