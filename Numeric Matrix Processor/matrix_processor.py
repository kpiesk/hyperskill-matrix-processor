def get_matrix(rows, columns):
    matrix_list = []
    for i in range(rows):
        row = input().split()
        matrix_list.append([])
        for j in range(columns):
            matrix_list[i].append(int(row[j]))
    return matrix_list


def add_matrices():
    dimensions_1 = [int(x) for x in input().split()]
    matrix_1 = get_matrix(dimensions_1[0], dimensions_1[1])
    dimensions_2 = [int(x) for x in input().split()]
    matrix_2 = get_matrix(dimensions_2[0], dimensions_2[1])

    if dimensions_1 == dimensions_2:
        matrices_sum = []
        for i in range(dimensions_1[0]):
            matrices_sum.append([])
            for j in range(dimensions_1[1]):
                matrices_sum[i].append(matrix_1[i][j] + matrix_2[i][j])
        print_matrix(matrices_sum)
    else:
        print('ERROR')


def multiply_by_constant():
    dimensions = [int(x) for x in input().split()]
    matrix = get_matrix(dimensions[0], dimensions[1])

    constant = int(input())
    matrix_result = []

    for i in range(dimensions[0]):
        matrix_result.append([])
        for j in range(dimensions[1]):
            matrix_result[i].append(matrix[i][j] * constant)
    print_matrix(matrix_result)


def print_matrix(matrix):
    for row in matrix:
        print(*row)


# add_matrices()
multiply_by_constant()