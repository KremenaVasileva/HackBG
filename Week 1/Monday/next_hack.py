def palindrome(obj):
    obj = str(obj)
    obj_length = len(obj)

    for i in range(0, obj_length // 2):
        if obj[i] != obj[obj_length - 1]:
            return False
        obj_length -= 1
    return True


def is_hack(n):
    binary_n = bin(n)[2::]
    string_bin_n = str(binary_n)
    counter = 0
    for i in range(0, len(string_bin_n)):
        if string_bin_n[i] == '1':
            counter += 1

    if palindrome(binary_n) == True and counter % 2 == 1:
        return True
    else:
        return False


def next_hack(n):
    result = n + 1
    if is_hack(result) == True:
        return result
    else:
        while is_hack(result) == False:
            result += 1
        return result

print (next_hack(8031))
