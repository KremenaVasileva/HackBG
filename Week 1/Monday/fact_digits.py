def factorial(n):
    factorial = 1
    if n <= 0 or n == 1:
        return 1
    else:
        while n != 1:
            factorial *= n
            n -= 1
        return factorial


def fact_digits(n):
    summed = 0
    while n != 0:
        summed += factorial(n % 10)
        n = n // 10
    return summed

n = int(input("Enter num: "))
print (fact_digits(n))
