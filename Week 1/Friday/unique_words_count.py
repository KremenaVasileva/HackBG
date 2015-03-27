def count_words(arr):
    result = {}
    for element in arr:
        if element in result:
            result[element] += 1
        else:
            result[element] = 1
    return result


def unique_words_count(arr):
    words = count_words(arr)
    count = 0
    for element in words:
        count += 1
    return count

print (unique_words_count(["apple", "banana", "apple", "pie"]))
print (unique_words_count(["python", "python", "python", "ruby"]))
