def is_number_balanced(n):
    n = str(n)
    first_sum = second_sum = 0
    if len(n) % 2 == 1:
        for i in range(0, len(n) // 2):
            first_sum += int(n[i])
        for i in range(len(n) // 2 + 1, len(n)):
            second_sum += int(n[i])
    else:
        for i in range(0, len(n) // 2):
            first_sum += int(n[i])
        for i in range(len(n) // 2, len(n)):
            second_sum += int(n[i])
    if first_sum == second_sum:
        return True
    else:
        return False

print (is_number_balanced(1238033))
