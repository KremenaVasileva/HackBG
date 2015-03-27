def count_words(arr):
    result = {}
    for element in arr:
        if element in result:
            result[element] += 1
        else:
            result[element] = 1
    return result

print (count_words(["python", "python", "python", "ruby"]))
