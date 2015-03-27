def palindrome(obj):
    obj = str(obj)
    obj_length = len(obj)

    for i in range(0, obj_length // 2):
        if obj[i] != obj[obj_length - 1]:
            return False

        obj_length -= 1
    return True


def reversed_int(n):
    return int(str(n)[::-1])


def p_score(n):
    result = 0
    if palindrome(n) == True:
        result += 1
    else:
        result += 1 + p_score(n + reversed_int(n))
    return result

num = 198
print (p_score(num))
