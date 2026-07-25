import unittest

from services import (
    Customer,
    BankAccount,
    SavingsAccount,
    CurrentAccount,
)


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        BankAccount.accounts.clear()
        BankAccount.total_accounts = 0
        BankAccount.next_account_number = 1001

    # 1
    def test_customer_creation(self):
        customer = Customer("Sanal", "9876543210")

        self.assertEqual(customer.name, "Sanal")
        self.assertEqual(customer.phone, "9876543210")

    # 2
    def test_create_bank_account(self):
        customer = Customer("Sanal", "9876543210")
        account = BankAccount("1001", customer, 1000)

        self.assertEqual(account.check_balance(), 1000)

    # 3
    def test_deposit(self):
        customer = Customer("Sanal", "9876543210")
        account = BankAccount("1001", customer, 1000)

        account.deposit(500)

        self.assertEqual(account.check_balance(), 1500)

    # 4
    def test_withdraw(self):
        customer = Customer("Sanal", "9876543210")
        account = BankAccount("1001", customer, 1000)

        account.withdraw(300)

        self.assertEqual(account.check_balance(), 700)

    # 5
    def test_invalid_deposit(self):
        customer = Customer("Sanal", "9876543210")
        account = BankAccount("1001", customer, 1000)

        result = account.deposit(-100)

        self.assertFalse(result)

    # 6
    def test_invalid_withdraw(self):
        customer = Customer("Sanal", "9876543210")
        account = BankAccount("1001", customer, 1000)

        result = account.withdraw(2000)

        self.assertFalse(result)

    # 7
    def test_duplicate_account_number(self):
        customer1 = Customer("A", "111")
        customer2 = Customer("B", "222")

        BankAccount("1001", customer1, 1000)

        with self.assertRaises(ValueError):
            BankAccount("1001", customer2, 500)

    # 8
    def test_total_accounts(self):
        customer1 = Customer("A", "111")
        customer2 = Customer("B", "222")

        BankAccount("1001", customer1)
        BankAccount("1002", customer2)

        self.assertEqual(BankAccount.get_total_accounts(), 2)

    # 9
    def test_find_account(self):
        customer = Customer("Sanal", "9876543210")
        account = BankAccount("1001", customer)

        found = BankAccount.find_account("1001")

        self.assertEqual(found, account)

    # 10
    def test_generate_account_number(self):
        number1 = BankAccount.generate_account_number()
        number2 = BankAccount.generate_account_number()

        self.assertEqual(number1, "1001")
        self.assertEqual(number2, "1002")


if __name__ == "__main__":
    unittest.main(verbosity=2)