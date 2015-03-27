def is_an_bn(word):
    count = word.count("a")
    if word == "a" * count + "b" * count:
        return True
    return False

print (is_an_bn("aaabbb"))
