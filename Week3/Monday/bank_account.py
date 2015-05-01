class BankAccount():

    def __init__(self, name, balance, currency):
        self.name = name
        self.balance = balance
        self.currency = currency
        self.account_history = []
        self.account_history.append("Account was created")

    def __str__(self):
        return "Bank account for {} with balance of {}{}".format(
            self.name, self.balance, self.currency)

    def __int__(self):
        self.account_history.append("__int__ check -> {}{}".format(
            self.get_balance(), self.currency))
        return int(self.balance)

    def deposit(self, amount):
        if amount < 0:
            raise ValueError
        else:
            self.balance += amount
            self.account_history.append("{}{} was deposited".format(
                amount, self.currency))

    def get_balance(self):
        self.account_history.append("Balance check -> {}{}".format(
            int(self.balance), self.currency))
        return self.balance

    def withdraw(self, amount):
        if self.balance < amount:
            self.account_history.append("Withdraw for {}{} failed".format(
                amount, self.currency))
            return False
        else:
            self.balance -= amount
            self.account_history.append("{}{} was withdrawn".format(
                amount, self.currency))
            return True

    def transfer_to(self, other, amount):
        if self.currency != other.currency or self.balance < amount:
            raise ValueError
        else:
            self.balance -= amount
            self.account_history.append("Transfer to {} for {}{}".format(
                other.name, amount, self.currency))

            other.balance += amount
            other.account_history.append("Transfer from {} for {}{}".format(
                self.name, amount, self.currency))
            return True

    def history(self):
        return self.account_history
