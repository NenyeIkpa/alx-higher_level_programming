#!/usr/bin/python3

"""
    Given a matrix, divides all the elements in it
"""


def matrix_divided(matrix, div):
    """divides all elements in matrix by div"""
    if type(matrix) is None or not isinstance(matrix, list) or len(matrix) == 0:
        raise (TypeError("matrix must be a matrix(list of lists) of integers/floats"))
    sub_len = []
    for i in range(len(matrix)):
        if not isinstance(matrix[i], list) or len(matrix[i]) is 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        sub_len.append(len(matrix[i]))
        if not all(num == sub_len[0] for num in sub_len):
            raise TypeError("Each row of the matrix must have the same size")
        for j in matrix[i]:
            if type(j) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for i in matrix:
        submatrix = []
        for j in i:
            submatrix.append(round(j / div, 2))
        new_matrix.append(submatrix)
    return new_matrix
