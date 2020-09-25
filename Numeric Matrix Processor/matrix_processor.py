def matrix_processor():
    user_menu()


def user_menu():
    while True:
        action = int(input('1. Add matrices\n'
                           '2. Multiply matrix by a constant\n'
                           '3. Multiply matrices\n'
                           '4. Transpose matrix\n'
                           '0. Exit\n'
                           'Your choice: '))
        if action == 1:
            matrix_1 = get_matrix(1)
            matrix_2 = get_matrix(2)
            add_matrices(matrix_1, matrix_2)
        elif action == 2:
            matrix = get_matrix()
            multiply_by_constant(matrix)
        elif action == 3:
            matrix_1 = get_matrix(1)
            matrix_2 = get_matrix(2)
            multiply_matrices(matrix_1, matrix_2)
        elif action == 4:
            transpose_matrix()
        elif action == 0:
            exit()


def get_matrix(number=None):
    if number == 1:
        input_text_size = 'Enter size of first matrix: '
        input_text_matrix = 'Enter first matrix:'
    elif number == 2:
        input_text_size = 'Enter size of second matrix: '
        input_text_matrix = 'Enter second matrix:'
    else:
        input_text_size = 'Enter size of matrix: '
        input_text_matrix = 'Enter matrix:'

    rows, columns = [int(x) for x in input(input_text_size).split()]
    print(input_text_matrix)
    matrix = []
    for i in range(rows):
        row = input().split()
        matrix.append([])
        for j in range(columns):
            matrix[i].append(check_type(row[j]))
    return matrix


def add_matrices(matrix_1, matrix_2):
    rows_1 = len(matrix_1)
    cols_1 = len(matrix_1[0])
    rows_2 = len(matrix_2)
    cols_2 = len(matrix_2[0])

    if rows_1 == rows_2 & cols_1 == cols_2:
        matrices_sum = []
        for i in range(rows_1):
            matrices_sum.append([])
            for j in range(cols_1):
                matrices_sum[i].append(matrix_1[i][j] + matrix_2[i][j])
        print_matrix(matrices_sum)
    else:
        print('ERROR')


def multiply_by_constant(matrix):
    matrix_result = []
    rows = len(matrix)
    cols = len(matrix[0])

    constant = check_type(input('Enter constant: '))

    for i in range(rows):
        matrix_result.append([])
        for j in range(cols):
            matrix_result[i].append(matrix[i][j] * constant)
    print_matrix(matrix_result)


def multiply_matrices(matrix_1, matrix_2):
    rows_1 = len(matrix_1)
    cols_1 = len(matrix_1[0])
    rows_2 = len(matrix_2)
    cols_2 = len(matrix_2[0])

    if cols_1 == rows_2:
        matrices_product = []
        for i in range(rows_1):
            matrices_product.append([])
            for j in range(cols_2):
                dot_product = 0
                for k in range(rows_2):
                    dot_product += matrix_1[i][k] * matrix_2[k][j]
                matrices_product[i].append(dot_product)
        print_matrix(matrices_product)
    else:
        print('ERROR')


def transpose_matrix():
    trans_action = int(input('1. Main diagonal\n'
                             '2. Side diagonal\n'
                             '3. Vertical line\n'
                             '4. Horizontal line\n'
                             'Your choice: '))

    if 1 <= trans_action <= 4:
        matrix = get_matrix()

        if trans_action == 1:
            transpose_main(matrix)
        elif trans_action == 2:
            transpose_side(matrix)
        elif trans_action == 3:
            transpose_vertical(matrix)
        elif trans_action == 4:
            transpose_horizontal(matrix)


# performs transposition along the main diagonal
def transpose_main(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    trans_matrix = []

    for i in range(rows):
        trans_matrix.append([])
        for j in range(cols):
            trans_matrix[i].append(matrix[j][i])
    print_matrix(trans_matrix)


# performs transposition along the side diagonal
def transpose_side(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    trans_matrix = []

    for i in range(rows):
        row = []
        for j in range(cols):
            row.insert(0, matrix[j][i])
        trans_matrix.insert(0, row)
    print_matrix(trans_matrix)


# performs transposition along the vertical line
def transpose_vertical(matrix):
    cols = len(matrix[0])
    trans_matrix = []

    for i in range(cols):
        trans_matrix.append(matrix[i][::-1])
    print_matrix(trans_matrix)


# performs transposition along the horizontal line
def transpose_horizontal(matrix):
    cols = len(matrix[0])
    trans_matrix = []

    for i in range(cols):
        trans_matrix.insert(0, matrix[i])
    print_matrix(trans_matrix)


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
