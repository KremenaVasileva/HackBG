def prepare_meal(number):
    n = 0
    temp = number
    result = ""
    while temp / 3 == temp // 3:
        n += 1
        temp /= 3
    if temp == 1:
        result += "spam " * n
    else:
        n = 0
    if n == 0 and number % 5 == 0:
        result += "eggs"
    elif number % 5 == 0:
        result += "and eggs"
    return result

print(prepare_meal(5))
