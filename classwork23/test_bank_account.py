import unittest
import bank_account


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = bank_account.BankAccount("Anri", 100)

    def test_initialization(self):
        self.assertEqual(self.account.owner, "Anri")
        self.assertEqual(self.account.balance, 100)

    def test_deposit_successful(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)

    def test_deposit_invalid_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-10)
        with self.assertRaises(ValueError):
            self.account.deposit(0)

    def test_withdraw_successful(self):
        self.account.withdraw(50)
        self.assertEqual(self.account.balance, 50)

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(150)

    def test_withdraw_invalid_amount(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-10)
        with self.assertRaises(ValueError):
            self.account.withdraw(0)


if __name__ == '__main__':
    unittest.main()