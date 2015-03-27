def contain_digit(number, digit):
    while number != 0:
        new_digit = number % 10
        if new_digit == digit:
            return True
            break
        number //= 10
    return False


def contains_digits(number, digits):
    for i in range(0, len(digits)):
        if contain_digit(number, digits[i]) == False:
            return False
            break
    return True

print (contains_digits(456, []))
