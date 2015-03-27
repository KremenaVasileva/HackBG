def to_number(digits):
    digits = digits[::-1]
    result = 0
    counter = 0
    for i in range(0, len(digits)):
        result += int(digits[i]) * (10 ** counter)
        counter += 1
    return result

num = ['1', '5', '6', '9']

print (to_number(num))
