def to_digits(n):
    n = int(n)
    list_of_digits = []
    while n != 0:
        digit = n % 10
        list_of_digits.append(digit)
        n = n // 10
    return list_of_digits[::-1]

num = int(input("Enter a num: "))
print (to_digits(num))
