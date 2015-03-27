def groupby(func, seq):
    func_results = []
    result = {}
    for i in range(0, len(seq)):
        func_results.append(func(seq[i]))
        if func(seq[i]) in result:
            result[func(seq[i])]. append(seq[i])
        else:
            result[func(seq[i])] = [seq[i]]
    return result

print (groupby(lambda x: x % 2, [0, 1, 2, 3, 4, 5, 6, 7]))
