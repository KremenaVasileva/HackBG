def sum_of_digits(n):
    summed = 0
    n = abs(n)
    while n != 0:
        summed += n % 10
        n = n // 10
    return summed

n = int(input("Enter num: "))
print (sum_of_digits(n))
