from config.config import load_settings
from config.environment import load_environment
from utils.validator import validate
from utils.logger import logger

from services import Customer, BankAccount, SavingsAccount, CurrentAccount

def get_input(prompt, data_type=str):
    while True:
        try:
            value = input(prompt)

            if data_type == int:
                return int(value)
            elif data_type == float:
                return float(value)

            return value

        except ValueError:
            print("Invalid input. Please try again.")
        except KeyboardInterrupt:
            print("\nInput cancelled.")
        except EOFError:
            print("\nUnexpected input.")


def get_account():
    account_number = get_input("Enter account number: ")
    account = BankAccount.find_account(account_number)

    if not account:
        print("Account not found.")

    return account

def application(config):
    APP_NAME = config.application_name
    BANK_NAME = config.bank_name

    print(f"Opening {APP_NAME}")
    print(f"Welcome to {BANK_NAME}")

    while True:
        print("\n===== Main Menu =====")
        print("1. Create New Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Total Accounts")
        print("6. Exit")

        choice = input("Select an option: ")

        match choice:
            case "1":
                print("Creating a new account...")

                account_number = BankAccount.generate_account_number()
                customer_name = get_input("Enter your name: ")
                customer_phone = get_input("Enter your phone number: ")

                customer = Customer(customer_name, customer_phone)
                
                initial_balance = get_input("Enter the initial balance: ", float)

                account_type = get_input("Enter account type (savings/current): ").lower()

                try:
                    if account_type == "savings":
                        account = SavingsAccount(account_number, customer, initial_balance)

                    elif account_type == "current":
                        account = CurrentAccount(account_number, customer, initial_balance)

                    else:
                        print("Invalid account type.")
                        continue

                except ValueError as e:
                    print(e)
                    continue

                BankAccount.save_accounts()
                print("Account created successfully!")
                print(account)
                

                for account_number, account in BankAccount.accounts.items():
                    print(account_number)
                    print(account)

            case "2":
                account = get_account()

                if not account:
                    continue

                amount = get_input("Enter amount to deposit: ", float)

                if account.deposit(amount):
                    BankAccount.save_accounts()
                    print("Deposit successful!")
                    print(account)

            case "3":
                account = get_account()

                if not account:
                    continue

                amount = get_input("Enter amount to withdraw: ", float)

                if account.withdraw(amount):
                    BankAccount.save_accounts()
                    print("Withdrawal successful!")
                    print(account)

            case "4":
                account = get_account()

                if not account:
                    continue

                print(f"Balance: ₹{account.check_balance()}")

            case "5":
                print(f"Total Accounts: {BankAccount.get_total_accounts()}")

            case "6":
                print("Thank you for using the banking system.")
                break

            case _:
                print("Invalid option. Please try again.")

def main():
    logger.info("Application Started")
    config = load_settings()
    environment = load_environment()

    BankAccount.load_accounts() 

    if not validate(config, environment):
        return

    application(config)

if __name__ == "__main__":
    main()