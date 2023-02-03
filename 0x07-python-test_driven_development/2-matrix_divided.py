#!/usr/bin/python3

"""matrix divided module"""


def matrix_divided(matrix, div):
    """matrix divided function

    Args:
        matrix (list): matrix to be divided
        div: divider number

    """
    if not isinstance(matrix, list) or True in [
            not isinstance(i, list) for i in matrix] or True in [
                True in k for k in [
                    [not (isinstance(j, int) | isinstance(j, float))
                     for j in i]
                    for i in matrix]]:

        raise (TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"))

    for i in matrix:
        temp = matrix.index(i) - 1
        idx = temp if temp >= 0 else 0
        if len(matrix[idx]) != len(i):
            raise (TypeError("Each row of the matrix must have the same size"))

    if not (isinstance(div, int) or isinstance(div, float)):
        raise (TypeError("div must be a number"))

    if div == 0:
        raise (ZeroDivisionError("division by zero"))

    result = list(list(round(j/div, 2) for j in i) for i in matrix)
    return (result)


if __name__ == '__main__':
    li = [[2]]
    print(matrix_divided(li, 3))
