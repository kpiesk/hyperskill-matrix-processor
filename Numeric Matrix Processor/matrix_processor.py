error = 'The operation cannot be performed'


def matrix_processor():
    user_menu()


def user_menu():
    while True:
        action = int(input('1. Add matrices\n'
                           '2. Multiply matrix by a constant\n'
                           '3. Multiply matrices\n'
                           '4. Transpose matrix\n'
                           '5. Calculate a determinant\n'
                           '0. Exit\n'
                           'Your choice: '))
        if action == 1:
            add_matrices(get_matrix(1), get_matrix(2))
        elif action == 2:
            multiply_by_constant(get_matrix())
        elif action == 3:
            multiply_matrices(get_matrix(1), get_matrix(2))
        elif action == 4:
            transpose_matrix()
        elif action == 5:
            print(f'The result is:\n{calc_determinant(get_matrix())}\n')
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
        print(error)


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
        print(error)


def transpose_matrix():
    trans_action = int(input('1. Main diagonal\n'
                             '2. Side diagonal\n'
                             '3. Vertical line\n'
                             '4. Horizontal line\n'
                             'Your choice: '))

    if 1 <= trans_action <= 4:
        if trans_action == 1:
            transpose_main(get_matrix())
        elif trans_action == 2:
            transpose_side(get_matrix())
        elif trans_action == 3:
            transpose_vertical(get_matrix())
        elif trans_action == 4:
            transpose_horizontal(get_matrix())


# calculates the determinant of a matrix
def calc_determinant(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    det = 0

    if rows != cols:  # determinant is defined only for square matrices
        print(error)
    else:
        if rows == 1:
            det = matrix[0][0]
        elif rows == 2:
            det = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        else:
            for j in range(cols):
                det += matrix[0][j] * calc_cofactor(matrix, 0, j)
        return det


# calculates the cofactor of the given row and column
def calc_cofactor(matrix, row, col):
    return pow((-1), row + 1 + col + 1) * calc_determinant(get_minor(matrix, row, col))


# getting a submatrix by deleting the corresponding rows and columns from the original matrix
def get_minor(matrix, delete_row, delete_col):
    minor_matrix = []
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        minor_matrix.append([])
        for j in range(cols):
            if i != delete_row and j != delete_col:
                minor_matrix[i].append(matrix[i][j])

    return [row for row in minor_matrix if row]  # returning a matrix without empty rows


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
