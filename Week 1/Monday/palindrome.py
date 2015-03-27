def palindrome(obj):
    obj = str(obj)
    if len(obj) % 2 == 0:
        first_half = obj[:len(obj) // 2]
        second_half = obj[len(obj) // 2::]
        second_half = second_half[::-1]
    else:
        first_half = obj[:len(obj) // 2]
        second_half = obj[len(obj) // 2 + 1::]
        second_half = second_half[::-1]
    if first_half == second_half:
        return True
    else:
        return False

print (palindrome("kaka"))
