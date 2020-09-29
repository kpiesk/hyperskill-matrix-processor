operation_error = 'The operation cannot be performed.'
input_error = 'Incorrect input.'


def matrix_processor():
    ui()


def ui():
    while True:
        action = int(input('1. Add matrices\n'
                           '2. Multiply matrix by a constant\n'
                           '3. Multiply matrices\n'
                           '4. Transpose matrix\n'
                           '5. Calculate a determinant\n'
                           '6. Inverse matrix\n'
                           '0. Exit\n'
                           'Your choice: '))
        if action == 1:
            print_matrix(add_matrices(get_matrix(1), get_matrix(2)))
        elif action == 2:
            print_matrix(multiply_by_constant(
                get_matrix(), check_type(input('Enter constant: '))))
        elif action == 3:
            print_matrix(multiply_matrices(get_matrix(1), get_matrix(2)))
        elif action == 4:
            transpose_matrix()
        elif action == 5:
            print(f'The result is:\n{calc_determinant(get_matrix())}\n')
        elif action == 6:
            print_matrix(inverse_matrix(get_matrix()))
        elif action == 0:
            exit()
        else:
            print(input_error)


# Gets the matrix from the user
def get_matrix(matrix_number=None):
    if matrix_number == 1:
        size_input_text = 'Enter size of first matrix: '
        matrix_input_text = 'Enter first matrix:'
    elif matrix_number == 2:
        size_input_text = 'Enter size of second matrix: '
        matrix_input_text = 'Enter second matrix:'
    else:
        size_input_text = 'Enter size of matrix: '
        matrix_input_text = 'Enter matrix:'

    rows, columns = [int(x) for x in input(size_input_text).split()]
    print(matrix_input_text)
    matrix = []
    for i in range(rows):
        row = input().split()
        matrix.append([])
        for j in range(columns):
            matrix[i].append(check_type(row[j]))
    return matrix


# Performs matrices addition
def add_matrices(matrix_1, matrix_2):
    rows_1, cols_1 = [x for x in get_matrix_size(matrix_1)]
    rows_2, cols_2 = [x for x in get_matrix_size(matrix_2)]

    # addition can only be performed if both matrices are the same size
    if rows_1 == rows_2 & cols_1 == cols_2:
        matrices_sum = []
        for i in range(rows_1):
            matrices_sum.append([])
            for j in range(cols_1):
                matrices_sum[i].append(matrix_1[i][j] + matrix_2[i][j])
        return matrices_sum
    else:
        print(operation_error)


# Performs matrix multiplication by a scalar
def multiply_by_constant(matrix, constant):
    rows, cols = [x for x in get_matrix_size(matrix)]
    matrix_product = []

    for i in range(rows):
        matrix_product.append([])
        for j in range(cols):
            matrix_product[i].append(matrix[i][j] * constant)
    return matrix_product


# Performs matrices multiplication
def multiply_matrices(matrix_1, matrix_2):
    rows_1, cols_1 = [x for x in get_matrix_size(matrix_1)]
    rows_2, cols_2 = [x for x in get_matrix_size(matrix_2)]

    # matrix multiplication can only be performed if the number of columns
    # in the first matrix equals the number of rows for the second matrix
    if cols_1 == rows_2:
        matrices_product = []
        for i in range(rows_1):
            matrices_product.append([])
            for j in range(cols_2):
                dot_product = 0
                for k in range(rows_2):
                    dot_product += matrix_1[i][k] * matrix_2[k][j]
                matrices_product[i].append(dot_product)
        return matrices_product
    else:
        print(operation_error)


# Performs user specified matrix transposition
def transpose_matrix():
    trans_action = int(input('1. Main diagonal\n'
                             '2. Side diagonal\n'
                             '3. Vertical line\n'
                             '4. Horizontal line\n'
                             'Your choice: '))

    if 1 <= trans_action <= 4:
        if trans_action == 1:
            print_matrix(transpose_main(get_matrix()))
        elif trans_action == 2:
            print_matrix(transpose_side(get_matrix()))
        elif trans_action == 3:
            print_matrix(transpose_vertical(get_matrix()))
        elif trans_action == 4:
            print_matrix(transpose_horizontal(get_matrix()))
    else:
        print(input_error)


# Calculates the determinant of a matrix
def calc_determinant(matrix):
    rows, cols = [x for x in get_matrix_size(matrix)]
    det = 0

    if rows != cols:  # determinant is defined only for square matrices
        print(operation_error)
    else:
        if rows == 1:
            det = matrix[0][0]
        elif rows == 2:
            det = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        else:
            for j in range(cols):
                det += matrix[0][j] * calc_cofactor(matrix, 0, j)
        return det


# Inverses the matrix
def inverse_matrix(matrix):
    if calc_determinant(matrix) == 0:
        print("This matrix doesn't have an inverse.\n")
    else:
        rows, cols = [x for x in get_matrix_size(matrix)]
        trans_matrix = transpose_main(matrix)
        cofactors_matrix = []
        for i in range(rows):
            cofactors_matrix.append([])
            for j in range(cols):
                cofactors_matrix[i].append(calc_cofactor(trans_matrix, i, j))

        return multiply_by_constant(
            cofactors_matrix, 1 / calc_determinant(matrix))


# Calculates the cofactor of the given row and column
def calc_cofactor(matrix, row, col):
    return pow((-1), row + 1 + col + 1) * calc_determinant(get_minor(matrix, row, col))


# Obtains a submatrix by deleting the corresponding rows and columns
def get_minor(matrix, delete_row, delete_col):
    rows, cols = [x for x in get_matrix_size(matrix)]
    minor_matrix = []

    for i in range(rows):
        minor_matrix.append([])
        for j in range(cols):
            if i != delete_row and j != delete_col:
                minor_matrix[i].append(matrix[i][j])

    # returning a matrix without empty rows
    return [row for row in minor_matrix if row]


# Performs transposition along the main diagonal
def transpose_main(matrix):
    rows, cols = [x for x in get_matrix_size(matrix)]
    trans_matrix = []

    for i in range(rows):
        trans_matrix.append([])
        for j in range(cols):
            trans_matrix[i].append(matrix[j][i])

    return trans_matrix


# Performs transposition along the side diagonal
def transpose_side(matrix):
    rows, cols = [x for x in get_matrix_size(matrix)]
    trans_matrix = []

    for i in range(rows):
        row = []
        for j in range(cols):
            row.insert(0, matrix[j][i])
        trans_matrix.insert(0, row)
    return trans_matrix


# Performs transposition along the vertical line
def transpose_vertical(matrix):
    cols = len(matrix[0])
    trans_matrix = []

    for i in range(cols):
        trans_matrix.append(matrix[i][::-1])
    return trans_matrix


# Performs transposition along the horizontal line
def transpose_horizontal(matrix):
    cols = len(matrix[0])
    trans_matrix = []

    for i in range(cols):
        trans_matrix.insert(0, matrix[i])
    return trans_matrix


# Checks whether the user entered number is int or float, and
# returns the input converted to the corresponding type
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


# Returns matrix size (rows and columns)
def get_matrix_size(matrix):
    return [len(matrix), len(matrix[0])]


def print_matrix(matrix):
    print('The result is:')
    for row in matrix:
        print(*row)
    print()


matrix_processor()
