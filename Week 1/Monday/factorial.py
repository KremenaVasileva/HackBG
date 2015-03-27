def factorial(n):
    factorial = 1
    if n <= 0 or n == 1:
        return 1
    else:
        while n != 1:
            factorial *= n
            n -= 1
        return factorial

n = int(input("Enter num: "))
print (factorial(n))
