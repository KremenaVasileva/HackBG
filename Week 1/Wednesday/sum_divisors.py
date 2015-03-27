def sum_of_divisors(n):
    result = 0
    for number in range(1, n + 1):
        if n % number == 0:
            result += number
    return result

print (sum_of_divisors(1000))
