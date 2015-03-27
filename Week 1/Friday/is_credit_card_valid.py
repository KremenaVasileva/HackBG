def is_credit_card_valid(number):
    number = str(number)
    new_num = ""
    if len(number) % 2 == 0:
        return False
    for i in range(0, len(number)):
            if i % 2 == 1:
                new_num += str(int(number[i]) * 2)
            else:
                new_num += number[i]
    summed = sum([int(x) for x in new_num])
    if summed % 10 == 0:
        return True
    return False

print(is_credit_card_valid(79927398713))
print(is_credit_card_valid(79927398715))
