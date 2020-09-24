def matrix_processor():
    user_menu()


def user_menu():
    while True:
        user_choice = int(input('1. Add matrices\n'
                                '2. Multiply matrix by a constant\n'
                                '3. Multiply matrices\n'
                                '0. Exit\n'
                                'Your choice: '))
        if user_choice == 1:
            add_matrices()
        elif user_choice == 2:
            multiply_by_constant()
        elif user_choice == 3:
            multiply_matrices()
        elif user_choice == 0:
            exit()


def get_matrix(rows, columns, input_text):
    print(input_text)
    matrix = []
    for i in range(rows):
        row = input().split()
        matrix.append([])
        for j in range(columns):
            matrix[i].append(check_type(row[j]))
    return matrix


def get_dimensions(input_text):
    return [int(x) for x in input(input_text).split()]


def add_matrices():
    dimensions_1 = get_dimensions('Enter size of first matrix: ')
    matrix_1 = get_matrix(dimensions_1[0], dimensions_1[1], 'Enter first matrix:')
    dimensions_2 = get_dimensions('Enter size of second matrix: ')
    matrix_2 = get_matrix(dimensions_2[0], dimensions_2[1], 'Enter second matrix:')

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
    dimensions = get_dimensions('Enter size of matrix: ')
    matrix = get_matrix(dimensions[0], dimensions[1], 'Enter matrix:')

    constant = check_type(input('Enter constant: '))
    matrix_result = []

    for i in range(dimensions[0]):
        matrix_result.append([])
        for j in range(dimensions[1]):
            matrix_result[i].append(matrix[i][j] * constant)
    print_matrix(matrix_result)


def multiply_matrices():
    dimensions_1 = get_dimensions('Enter size of first matrix: ')
    matrix_1 = get_matrix(dimensions_1[0], dimensions_1[1], 'Enter first matrix:')
    dimensions_2 = get_dimensions('Enter size of second matrix: ')
    matrix_2 = get_matrix(dimensions_2[0], dimensions_2[1], 'Enter second matrix:')

    if dimensions_1[1] == dimensions_2[0]:
        matrices_product = []
        for i in range(dimensions_1[0]):
            matrices_product.append([])
            for j in range(dimensions_2[1]):
                dot_product = 0
                for k in range(dimensions_2[0]):
                    dot_product += matrix_1[i][k] * matrix_2[k][j]
                matrices_product[i].append(dot_product)
        print_matrix(matrices_product)
    else:
        print('ERROR')


def print_matrix(matrix):
    print('The result is:')
    for row in matrix:
        print(*row)
    print()


def check_type(number):
    try:
        int(number)
        return int(number)
    except ValueError:
        try:
            float(number)
            return float(number)
        except ValueError:
            return None


matrix_processor()
