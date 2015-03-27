def count_vowels(str):
    counter = 0
    for i in range(0, len(str)):
        if str[i] in "aeiouyAEIOUY":
            counter += 1
    return counter

print (count_vowels("grrrrgh!IY"))
