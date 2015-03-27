def sum_matrix(m):
    result = 0
    for i in range(0, len(m)):
        for element in m[i]:
            result += element
    return result


def substract(number_one, number_two):
    return min(number_one, number_two)


def top_left(m):
    return substract(m[0][0], m[0][1]) + substract(m[0][0], m[1][1]) + substract(m[0][0], m[1][0])


def top_right(m):
    p = len(m) - 1
    return substract(m[0][p], m[0][p - 1]) + substract(m[0][p], m[1][p - 1]) + substract(m[0][p], m[1][p])


def bottom_left(m):
    p = len(m) - 1
    return substract(m[p][0], m[p - 1][0]) + substract(m[p][0], m[p - 1][1]) + substract(m[p][0], m[p][1])


def bottom_right(m):
    p = len(m) - 1
    return substract(m[p][p], m[p - 1][p]) + substract(m[p][p], m[p - 1][p - 1]) + substract(m[p][p], m[p][p - 1])


def upper_row(m, j):
    damage = substract(m[0][j], m[0][j - 1]) + substract(m[0][j], m[0][j + 1])
    damage += substract(m[0][j], m[1][j - 1]) + substract(m[0][j], m[1][j]) + substract(m[0][j], m[1][j + 1])
    return damage


def bottom_row(m, j):
    p = len(m) - 1
    damage = substract(m[p][j], m[p][j - 1]) + substract(m[p][j], m[p][j + 1])
    damage += substract(m[p][j], m[p - 1][j - 1]) + substract(m[p][j], m[p - 1][j]) + substract(m[p][j], m[p - 1][j + 1])
    return damage


def left_col(m, i):
    damage = substract(m[i][0], m[i - 1][0]) + substract(m[i][0], m[i + 1][0])
    damage += substract(m[i][0], m[i - 1][1]) + substract(m[i][0], m[i][1]) + substract(m[i][0], m[i + 1][1])
    return damage


def right_col(m, i):
    p = len(m) - 1
    damage = substract(m[i][p], m[i - 1][p]) + substract(m[i][p], m[i + 1][p])
    damage += substract(m[i][p], m[i - 1][p - 1]) + substract(m[i][p], m[i][p - 1]) + substract(m[i][p], m[i + 1][p - 1])
    return damage


def middle(m, i, j):
    damage = substract(m[i][j], m[i - 1][j - 1]) + substract(m[i][j], m[i - 1][j]) + substract(m[i][j], m[i - 1][j + 1])
    damage += substract(m[i][j], m[i][j - 1]) + substract(m[i][j], m[i][j + 1])
    damage += substract(m[i][j], m[i + 1][j - 1]) + substract(m[i][j], m[i + 1][j]) + substract(m[i][j], m[i + 1][j + 1])
    return damage


def matrix_bombing_plan(m):
    damage = {}
    matrix_sum = sum_matrix(m)

    damage[(0, 0)] = matrix_sum - top_left(m)  # top left corner
    damage[(0, len(m) - 1)] = matrix_sum - top_right(m)  # top right corner
    damage[(len(m[0]) - 1, 0)] = matrix_sum - bottom_left(m)  # bottom left corner
    damage[(len(m) - 1, len(m[0]) - 1)] = matrix_sum - bottom_right(m)  # bottom right corner

    for j in range(1, len(m) - 2):  # upper and bottom row
        damage[(0, j)] = matrix_sum - upper_row(m, j)
        damage[(len(m) - 1, j)] = matrix_sum - bottom_row(m, j)

    for i in range(1, len(m[0]) - 2):  # left and right col
        damage[(i, 0)] = matrix_sum - left_col(m, i)
        damage[(i, len(m[0]) - 1)] = matrix_sum - right_col(m, i)

    for i in range(1, len(m[0]) - 2):
        for j in range(1, len(m) - 2):
            damage[(i, j)] = matrix_sum - middle(m, i, j)

    print (damage)

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_bombing_plan(m)
print (upper_row(m, 1))
