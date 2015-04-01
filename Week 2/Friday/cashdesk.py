class Bill:
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return "The bill is {}$".format(self.amount)

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return int(self.amount)

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(self):
        return hash(str(self.amount))


class BatchBill():
    def __init__(self, bills):
        self.bills = bills

    def __getitem__(self, i):
        return (self.bills)[i]

    def __len__(self):
        return len(self.bills)

    def total(self):
        total = 0
        for i in range(len(bills)):
            total += bills[i].__int__()
        return total


class CashDesk():
    def __init__(self):
        self.bills = []

    def take_money(self, money):
        if isinstance(money, Bill):
            self.bills.append(money.__int__())
        else:
            for bill in money:
                self.bills.append(int(bill))

    def total(self):
        total_amount = 0
        for bill in self.bills:
            total_amount += int(bill)

        return "The total amount is {}$".format(total_amount)

    def inspect(self):
        table_repr = {}
        for bill in self.bills:
            if bill in table_repr:
                table_repr[bill] += 1
            else:
                table_repr[bill] = 1
        for bill in sorted(table_repr):
            print ("{}$ bills - {}".format(str(bill), str(table_repr[bill])))

values = [10, 20, 50, 100, 100, 100]
bills = [Bill(value) for value in values]

batch = BatchBill(bills)

desk = CashDesk()

desk.take_money(Bill(10))
desk.take_money(batch)

print(desk.total())
desk.inspect()
