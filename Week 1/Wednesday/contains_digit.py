def contain_digit(number, digit):
    while number != 0:
        new_digit = number % 10
        if new_digit == digit:
            return True
            break
        number //= 10
    return False

print(contain_digit(1234, 5))
