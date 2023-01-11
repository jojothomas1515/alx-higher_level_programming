#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # first method is more pythonic
    # new_matrix = [list(map(lambda x:  x**2, j)) for j in matrix]

    # less pythonic
    new_matrix = list(map(lambda x: list((map(lambda y: y**2, x))), matrix))
    return (new_matrix)


if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    new_matrix = square_matrix_simple(matrix)
    print(new_matrix)
    print(matrix)
