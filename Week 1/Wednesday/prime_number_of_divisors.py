def is_prime(n):
    if n <= 1:
        return False
    for divisor in range(2, n // 2 + 1):
        if n % divisor == 0:
            return False
            break
    return True


def prime_number_of_divisors(n):
    counter = 0
    for number in range(1, n + 1):
        if n % number == 0:
            counter += 1
    return is_prime(counter)

print (prime_number_of_divisors(7))
