def is_prime(n):
    return (n + 1) == sum([x for x in range(1, n + 1) if n % x == 0])


def prime_factorization(n):
    divisors = [x for x in range(1, n + 1) if n % x == 0 and is_prime(x)]
    result = []
    for element in divisors:
        count = 0
        while n / element == n // element:
            count += 1
            n /= element
        result.append((element, count), )
    return result

print (prime_factorization(1000))
