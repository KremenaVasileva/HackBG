def sum_matrix(m):
    result = 0
    for i in range(0, len(m)):
        for element in m[i]:
            result += element
    return result

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]

print (sum_matrix(m))
print (sum_matrix(n))
