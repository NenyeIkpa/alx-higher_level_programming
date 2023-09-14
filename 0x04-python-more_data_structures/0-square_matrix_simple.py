#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Get the number of rows and columns in the matrix
    num_of_rows = len(matrix)
    num_of_columns = len(matrix[0])
    new_matrix = [[0] * num_of_columns for _ in range(num_of_rows)]

    # loop through the rows and columns, square each element and store it at same index in new_matrix
    for i in range(num_of_rows):
        for j in range(num_of_columns):
            new_matrix[i][j] = matrix[i][j] ** 2
    return new_matrix
