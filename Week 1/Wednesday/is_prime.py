def is_prime(n):
    if n <= 1:
        return False
    for divisor in range(2, n // 2 + 1):
        if n % divisor == 0:
            return False
            break
    return True

print (is_prime(4))
