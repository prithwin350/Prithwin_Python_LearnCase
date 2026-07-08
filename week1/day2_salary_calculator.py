def calculate_tax(gross_salary, tax_percent):
    return gross_salary * tax_percent / 100


def calculate_take_home(gross_salary, tax_amount):
    return gross_salary - tax_amount


def salary_calculator():
    print("Initializing the Salary Calculator...\n")

    name = input("Enter employee name: ")

    while True:
        try:
            gross_salary = float(input("Enter gross salary: "))
            tax_percent = float(input("Enter tax percentage: "))

            if not (0 <= tax_percent <= 100):
                print("Tax percentage must be between 0 and 100.\n")
                continue

            break

        except ValueError:
            print("Invalid input. Please enter numbers only.\n")

    tax_amount = calculate_tax(gross_salary, tax_percent)
    take_home = calculate_take_home(gross_salary, tax_amount)

    print(f"Employee    : {name}")
    print(f"Gross Salary: ₹{gross_salary:.2f}")
    print(f"Tax Percent : {tax_percent}%")
    print(f"Tax Amount  : ₹{tax_amount:.2f}")
    print(f"Take Home   : ₹{take_home:.2f}")


def main():
    print("Hello! Welcome to the Salary Calculator!\n")
    salary_calculator()


main()