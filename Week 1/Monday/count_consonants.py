def count_consonants(str):
    counter = 0
    for i in range(0, len(str)):
        if str[i] in "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ":
            counter += 1
    return counter

print (count_consonants("TheistareykjarbunGA"))
