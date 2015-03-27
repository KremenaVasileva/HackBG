def zero_insert(n):
    n = str(n)
    result = ""
    for i in range(0, len(n) - 1):
        left_digit = int(n[i])
        right_digit = int(n[i + 1])
        if left_digit == right_digit or left_digit + right_digit == 10:
            result += str(left_digit) + '0'
        else:
            result += str(left_digit)
    result += n[len(n) - 1]  # adding the last digit
    return int(result)

print (zero_insert(116457))
