from services.customer import Customer
from utils.json_handler import read_json, write_json

class BankAccount:
    total_accounts = 0
    next_account_number = 1001
    accounts = {}


    def __init__(self, account_number, customer, balance=0):
        if account_number in BankAccount.accounts:
            raise ValueError("Account number already exists.")

        self.account_number = account_number
        self.customer = customer
        self._balance = balance

        BankAccount.accounts[self.account_number] = self
        BankAccount.total_accounts += 1

    def __str__(self):
        return (
            f"Account Number : {self.account_number}\n"
            f"Account Holder : {self.customer.name}\n"
            f"Balance        : ₹{self._balance}"
        )

    def to_dict(self):
        return {
            "account_number": self.account_number,
            "customer": {
                "name": self.customer.name,
                "phone": self.customer.phone,
            },
            "balance": self._balance,
            "account_type": self.__class__.__name__,
        }

    
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

    @classmethod
    def generate_account_number(cls):
        account_number = str(cls.next_account_number)
        cls.next_account_number += 1
        return account_number


    @classmethod
    def load_accounts(cls):
        data = read_json()
        print("Data:", data)

        cls.accounts.clear()
        cls.total_accounts = 0

        highest_account_number = 1000

        for item in data:
            customer = Customer(
                item["customer"]["name"],
                item["customer"]["phone"],
            )

            account_type = item["account_type"]

            if account_type == "SavingsAccount":
                SavingsAccount(item["account_number"], customer, item["balance"])
            elif account_type == "CurrentAccount":
                CurrentAccount(item["account_number"], customer, item["balance"])
            else:
                BankAccount(item["account_number"], customer, item["balance"])

            highest_account_number = max(
                highest_account_number,
                int(item["account_number"])
            )

        cls.next_account_number = highest_account_number + 1


    @classmethod
    def save_accounts(cls):
        data = []

        for account in cls.accounts.values():
            data.append(account.to_dict())

        write_json(data)


class SavingsAccount(BankAccount):

    MINIMUM_BALANCE = 1000
    LOW_BALANCE_FINE = 100

    def withdraw(self, amount):

        if amount > self._balance:
            print("Insufficient balance.")
            return False

        self._balance -= amount

        if self._balance < SavingsAccount.MINIMUM_BALANCE:
            self._balance -= SavingsAccount.LOW_BALANCE_FINE

            print(
                f"Warning: Balance below minimum. "
                f"₹{SavingsAccount.LOW_BALANCE_FINE} fine applied."
            )

        return True


class CurrentAccount(BankAccount):

    OVERDRAFT_LIMIT = 10000
    OVERDRAFT_FEE = 500

    def withdraw(self, amount):

        if amount > self._balance + CurrentAccount.OVERDRAFT_LIMIT:
            print("Overdraft limit exceeded.")
            return False

        self._balance -= amount

        if self._balance < 0:
            self._balance -= CurrentAccount.OVERDRAFT_FEE

            print(
                f"Overdraft used. "
                f"₹{CurrentAccount.OVERDRAFT_FEE} fee applied."
            )

        return True
