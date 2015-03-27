def char_histogram(str):
    result = {}
    for i in range(0, len(str)):
        if str[i] in result.keys():
            result[str[i]] += 1
        else:
            result[str[i]] = 1
    return result

string = "AAAaaa!!!!!"

print (char_histogram(string))
