from datetime import datetime

class ReturnToMenu(Exception):
    pass

def get_input(message):
    value = input(message)

    if value.lower() == "exit":
        raise ReturnToMenu

    return value

def create_invoice_number(invoice_id, customer_name, invoice_date):
    formatted_id = invoice_id.zfill(4)
    formatted_customer = customer_name.split()[0].upper()
    parsed_date = datetime.strptime(invoice_date, "%d-%m-%Y")
    formatted_date = parsed_date.strftime("%Y%m%d")

    return f"INV-{formatted_id}-{formatted_customer}-{formatted_date}"

def invoice_formatter():
    print("This is the invoice formatter")

    try:
        while True:
            invoice_id = get_input("Enter Invoice ID (or 'exit' to return): ")
            customer_name = get_input("Enter Customer Name (or 'exit' to return): ")
            invoice_date = get_input("Enter Invoice Date (DD-MM-YYYY) (or 'exit' to return): ")

            try:
                invoice_number = create_invoice_number(invoice_id, customer_name, invoice_date)
                print(f"Formatted invoice: {invoice_number}")
                return
            except ValueError as error:
                print(error)
            except IndexError:
                print("Customer name cannot be empty.")

    except ReturnToMenu:
        return

def calculate_date_difference(start_date, end_date):
    parsed_start_date = datetime.strptime(start_date, "%d-%m-%Y")
    parsed_end_date = datetime.strptime(end_date, "%d-%m-%Y")
    difference = parsed_end_date - parsed_start_date

    difference_days = abs(difference.days)

    if difference_days >= 365:
        years = difference_days / 365
        return f"{difference_days} days ({years:.2f} years)"

    elif difference_days >= 30:
        months = difference_days / 30
        return f"{difference_days} days ({months:.2f} months)"

    return f"{difference_days} days"


def date_difference_calculator():
    print("Date Difference Calculator")

    try:
        while True:
            start_date = get_input("Enter Start Date (DD-MM-YYYY) (or 'exit' to return): ")
            end_date = get_input("Enter End Date (DD-MM-YYYY) (or 'exit' to return): ")

            try:
                difference = calculate_date_difference(start_date, end_date)
                print(f"Date difference: {difference}")
                return

            except ValueError as error:
                print(error)

    except ReturnToMenu:
        return



def application():
    while True:
        print("\n========== Application ==========")
        print("1. Invoice Formatter")
        print("2. Date Difference Calculator")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            invoice_formatter()
        elif choice == "2":
            date_difference_calculator()
        elif choice == "3":
            print("Application closed.")
            break
        else:
            print("Invalid choice.")


def main():
    application()

if __name__ == "__main__":
    main()