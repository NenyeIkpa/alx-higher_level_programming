#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # create and return a new matrix with squared of values of matrix
    """ new_matrix =
    [list(map(lambda num: num ** 2, sublist)) for sublist in matrix"""
    new_matrix = []
    for listed in matrix:
        new_list = []
        for num in listed:
            new_list.append(num ** 2)
        new_matrix.append(new_list)
    return (new_matrix)
