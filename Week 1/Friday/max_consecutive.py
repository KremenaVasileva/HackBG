def group(elements):
    new_list = []
    current_list = []
    current_list.append(elements[0])
    for i in range(1, len(elements)):
        if elements[i - 1] == elements[i]:
            current_list.append(elements[i])
        else:
            new_list.append(current_list)
            current_list = []
            current_list.append(elements[i])
    new_list.append(current_list)
    return new_list


def max_consecutive(items):
    items = group(items)
    result_list = [len(items[i]) for i in range(0, len(items))]
    return max(result_list)

print(max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]))
