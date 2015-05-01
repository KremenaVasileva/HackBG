from bank_account import BankAccount
import unittest


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.my_account = BankAccount("Rado", 2000, "$")
        self.name = "Rado"
        self.balance = 2000
        self.currency = "$"
        self.account_history = ["Account was created"]

        self.amount = 1000
        self.str_self = "Bank account for {} with balance of {}{}".format(
            self.name, self.balance, self.currency)
        self.other_account = BankAccount("Ivo", 50, "$")

    def test_init(self):
        self.assertTrue(isinstance(self.my_account, BankAccount))
        self.assertEqual(self.my_account.name, self.name)
        self.assertEqual(self.my_account.balance, self.balance)
        self.assertEqual(self.my_account.currency, self.currency)

    def test_deposit(self):
        current_balance = self.my_account.balance + self.amount
        self.my_account.deposit(self.amount)
        self.assertEqual(self.my_account.balance, current_balance)
        with self.assertRaises(ValueError):
            self.my_account.deposit(-20)

    def test_balance(self):
        self.assertEqual(self.my_account.get_balance(), self.balance)

    def test_str(self):
        self.assertEqual(str(self.my_account), self.str_self)

    def test_int(self):
        self.assertEqual(int(self.my_account), int(self.balance))

    def test_withdraw(self):
        self.my_account.balance = 50
        self.money_true = self.my_account.balance * 0.5
        self.money_false = self.my_account.balance * 2
        # money less than balance
        self.assertTrue(self.my_account.withdraw(self.money_true))
        # money more than balance
        self.assertFalse(self.my_account.withdraw(self.money_false))

        result = int(self.my_account.balance) - int(self.money_true)
        self.my_account.withdraw(self.money_true)
        self.assertEqual(self.my_account.get_balance(), result)

    def test_transfer_to_currency_and_amount(self):
        new_account = BankAccount("lala", 500, "GBP")
        other_account = BankAccount("balala", 50, "$")

        with self.assertRaises(ValueError):
            self.my_account.transfer_to(new_account, 60)
            self.my_account.transfer_to(other_account, 60)

    def test_transfer_to_deposited_and_withdrawn(self):
        money_transfered = 10
        withdrawn_result = int(self.my_account.balance) - money_transfered
        deposited_result = int(self.other_account.balance) + money_transfered

        self.my_account.transfer_to(self.other_account, money_transfered)
        self.assertEqual(self.my_account.get_balance(), withdrawn_result)
        self.assertEqual(self.other_account.get_balance(), deposited_result)

    def test_history(self):
        needed_result = ["Account was created", ]
        self.assertEqual(self.account_history, needed_result)

        self.my_account.deposit(20)
        needed_result.append("{}{} was deposited".format(
                20, self.my_account.currency))

        self.my_account.get_balance()
        needed_result.append("Balance check -> {}{}".format(
            2020, self.my_account.currency))  # 2000 + 20

        self.my_account.withdraw(5000)
        needed_result.append("Withdraw for 5000{} failed".format(
            self.my_account.currency))

        self.my_account.withdraw(200)
        needed_result.append("200{} was withdrawn".format(
            self.my_account.currency))

        self.my_account.transfer_to(self.other_account, 700)
        needed_result.append("Transfer to {} for 700{}".format(
            self.other_account.name, self.my_account.currency))

        self.assertEqual(self.my_account.history(), needed_result)

if __name__ == '__main__':
    unittest.main()
