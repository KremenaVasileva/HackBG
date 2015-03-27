def magic_square(matrix):
    matr_len = len(matrix)
    row_sum = [sum(matrix[i]) for i in range(0, matr_len)]
    col_sum = [0] * matr_len
    for j in range(0, len(matrix)):
        col_sum[j] = sum([matrix[i][j] for i in range(0, matr_len)])
    diag_one = sum([matrix[i][i] for i in range(0, matr_len)])
    diag_two = sum([matrix[i][matr_len - i - 1] for i in range(0, matr_len)])
    result = [row_sum == col_sum, diag_one == diag_two, row_sum[0] == diag_one]
    return all(result)

print(magic_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(magic_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]))
m = [[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]
print(magic_square(m))
