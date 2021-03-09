import numpy as np


def add_matrix():

    dimension = input('Enter size of first matrix: ').split()
    row1 = int(dimension[0])
    collum = int(dimension[1])
    print('Enter first matrix:')
    matrix1 = [input().split() for i in range(row1)]

    dimension2 = input('Enter size of second matrix:' ).split()
    row2 = int(dimension2[0])
    collum2 = int(dimension2[1])
    print('Enter second matrix:')
    matrix2 = [input().split() for i in range(row2)]
    if row1 == row2 and collum == collum2:
        new_matrix = [[(int(i1) if i1.isdigit() else float(i1)) + (int(j1) if j1.isdigit() else float(j1)) for i1, j1 in zip(i, j)] for i, j in zip(matrix1, matrix2)]
        print('The result is:')
        for elem in new_matrix:
            print(*elem, sep=" ")
    else:
        print('The operation cannot be performed.')


def menu():
    print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit""")
    user_2 = input('Your choice: ')
    if user_2 == "1":
        add_matrix()
    if user_2 == "2":
        matrix_multiplication_with_constant()
    if user_2 == "3":
        plane_matrix_multipication()
    if user_2 == "4":
        transpose_matrix()
    if user_2 == "5":
        determinant()
    if user_2 == "6":
        inverse()
    if user_2 == "0":
        exit_p()


def matrix_multiplication_with_constant():
    print('Enter size of matrix:')
    dimension = input().split()
    row1 = int(dimension[0])
    print('Enter matrix:')
    matrix = [input().split() for i in range(row1)]
    #print(matrix)
    print('Enter constant:')
    constant_input = input()
    constant = int(constant_input) if constant_input.isdigit() else float(constant_input)
    # row = int(dimension[0])
    # collum = int(dimension[1])
    new_mult_matrix = [[constant * (int(element) if element.isdigit() else float(element)) for element in row] for row in matrix]
    print('The result is:')
    for elem in new_mult_matrix:
        print(*elem, sep=" ")


def plane_matrix_multipication():
    dimension = input('Enter size of first matrix: ').split()
    row1 = int(dimension[0])
    collum = int(dimension[1])
    print('Enter first matrix:')
    matrix1 = [input().split() for i in range(row1)]
    # matrix1 = [list(map(int, matrix_input)) for matrix_input in matrix_input]

    dimension2 = input('Enter size of second matrix:').split()
    row2 = int(dimension2[0])
    collum2 = int(dimension2[1])
    print('Enter second matrix: ')
    matrix2 = [input().split() for i in range(row2)]
    # matrix2 = [list(map(int, matrix_input2)) for matrix_input2 in matrix_input2]
    if collum == row2:
        zip_b = zip(*matrix2)
        zip_b = list(zip_b)
        result_matrix = [[sum((int(ele_a) if ele_a.isdigit() else float(ele_a)) * (int(ele_b) if ele_b.isdigit() else float(ele_b)) for ele_a, ele_b in zip(row_a, col_b))for col_b in zip_b] for row_a in matrix1]
        # print(result_matrix)
        print('The result is:')
        for elem in result_matrix:
            print(*elem, sep=" ")
    else:
        print('The operation cannot be performed.')


def transpose_matrix():
    print('''1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line''')

    choice = input('Your choice: ')
    if choice == "1":
        transpose_main_diagonal()
    if choice == "2":
        transpose_side_diagonal()
    if choice == "3":
        transpose_vertical()
    if choice == "4":
        transpose_horizontal()


def transpose_main_diagonal():
    dimension = input('Enter matrix size: ').split()
    row = int(dimension[0])
    collum = int(dimension[1])
    print('Enter matrix:')
    str_matrix = [input().split() for i in range(row)]
    result = [[str_matrix[j][i] for j in range(len(str_matrix))] for i in range(len(str_matrix[0]))]
    for elem in result:
        print(*elem, sep=" ")

    # das war weil ich die matrix falsch eingegeben hab
    #int_matrix = x = [[int(j) for j in i] for i in str_matrix]
    # list_with_seperated_ints = []
    # i = 0
    # for nestlist in str_matrix:
    #     inner_list = []
    #     for elem in nestlist:
    #         for i in elem:
    #             inner_list.append(i)
    #         list_with_seperated_ints.append(inner_list)
    #
    # result = [[list_with_seperated_ints[j][i] for j in range(len(list_with_seperated_ints))] for i in
    #           range(len(list_with_seperated_ints[0]))]
    # print(result)
    # for elem in result:
    #     print(*elem, sep=" ")


def transpose_side_diagonal():
    dimension = input('Enter matrix size: ').split()
    row = int(dimension[0])
    collum = int(dimension[1])
    print('Enter matrix:')
    str_matrix = [input().split() for i in range(row)]
    n_matrix = np.array(str_matrix)

    bla = n_matrix[::-1, ::-1].T
    #print(bla)

    for elem in bla:
        print(*elem, sep=" ")



def transpose_vertical():
    dimension = input('Enter matrix size: ').split()
    row = int(dimension[0])
    collum = int(dimension[1])
    print('Enter matrix:')
    str_matrix = [input().split() for i in (range(row))]
    n_matrix = [li[::-1] for li in str_matrix]
    for elem in n_matrix:
        print(*elem, sep=" ")


def transpose_horizontal():
    dimension = input('Enter matrix size: ').split()
    row = int(dimension[0])
    collum = int(dimension[1])
    print('Enter matrix:')
    str_matrix = [input().split() for i in (range(row))]

    n_matrix = (str_matrix[::-1])
    for elem in n_matrix:
        print(*elem, sep=" ")


def determinant():
    dimension = input('Enter matrix size: ').split()
    row = int(dimension[0])
    print('Enter matrix:')
    str_matrix = [input().split() for i in (range(row))]
    n_matrix = np.array(str_matrix, dtype='float')
    # print(n_matrix)
    # det = np.linalg.det(n_matrix)

    print(np.linalg.det(n_matrix))


def inverse():
    dimension = input('Enter matrix size: ').split()
    row = int(dimension[0])
    print('Enter matrix:')
    str_matrix = [input().split() for i in (range(row))]
    x = np.array(str_matrix, dtype='float')
    try:
        result_matrix = np.linalg.inv(x)
    except np.linalg.LinAlgError:
        print("This matrix doesn't have an inverse.")
    else:
        print('The result is:')
        for elem in result_matrix:
            print(*elem, sep=" ")


def exit_p():
    exit()


while True:
    menu()
    print('\n')