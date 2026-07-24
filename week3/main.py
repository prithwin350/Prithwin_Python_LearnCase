from config.config import load_settings
from config.environment import load_environment
from utils.validator import validate
from utils.logger import logger



class BankAccount:
    total_accounts = 0
    accounts = {}
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self._balance = balance

        BankAccount.accounts[self.account_number] = self
        BankAccount.total_accounts += 1

    def __str__(self):
        return (
            f"Account Number : {self.account_number}\n"
            f"Account Holder : {self.account_holder}\n"
            f"Balance        : ₹{self._balance}"
        )

    
    @staticmethod
    def is_valid_amount(amount):
        if amount <= 0:
            print("Amount must be greater than zero.")
            return False

        return True

    
    def deposit(self, amount):
        if not BankAccount.is_valid_amount(amount):
            return False

        self._balance += amount
        return True


    def withdraw(self, amount):
        if not BankAccount.is_valid_amount(amount):
            return False

        if amount > self._balance:
            print("Insufficient balance.")
            return False

        self._balance -= amount
        return True

    def check_balance(self):
        return self._balance

    @classmethod
    def get_total_accounts(cls):
        return cls.total_accounts

    @classmethod
    def find_account(cls, account_number):
        return cls.accounts.get(account_number)


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

                account_number = get_input("Enter your account number: ")
                account_holder = get_input("Enter your name: ")
                initial_balance = get_input("Enter the initial balance: ", float)

                account = BankAccount(account_number, account_holder, initial_balance)

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
                    print("Deposit successful!")
                    print(account)

            case "3":
                account = get_account()

                if not account:
                    continue

                amount = get_input("Enter amount to withdraw: ", float)

                if account.withdraw(amount):
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

    if not validate(config, environment):
        return

    application(config)

if __name__ == "__main__":
    main()