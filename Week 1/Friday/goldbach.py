def is_prime(n):
    divisors_sum = sum([x for x in range(1, n + 1) if n % x == 0])
    return n + 1 == divisors_sum


def goldbach(n):
    result = []
    for i in range(1, n // 2 + 1):
        if is_prime(i) and is_prime(n - i):
            result.append((i, n - i), )
    return result

print (goldbach(100))
