class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.numerator, self.denominator = self.normalized()

    def __str__(self):
        return "{} / {}".format(self.numerator, self.denominator)

    def __repr__(self):
        return self.__str__()

    def normalized(self):
        for i in range(2, int(self.denominator) + 1):
            while self.denominator % i == 0 and self.numerator % i == 0:
                self.denominator /= i
                self.numerator /= i
        return int(self.numerator), int(self.denominator)

    def __add__(self, other):
        denominator = self.denominator * other.denominator
        numerator = self.numerator * other.denominator
        numerator += other.numerator * self.denominator
        return Fraction(numerator, denominator)

    def __sub__(self, other):
        denominator = self.denominator * other.denominator
        numerator = self.numerator * other.denominator
        numerator -= other.numerator * self.denominator
        return Fraction(numerator, denominator)

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __eq__(self, other):
        return self.normalized() == other.normalized()

a = Fraction(2, 2)
b = Fraction(2, 3)

print (a == b)
print (a - b)
print (a + b)
