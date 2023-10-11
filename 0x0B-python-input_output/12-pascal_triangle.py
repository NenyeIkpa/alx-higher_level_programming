#!/usr/bin/python3

""" creates Pscal's triangle """


def pascal_triangle(n):
    """ returns a Psacal's triangle """
    if n <= 0:
        return []
    triangle = [[1]]
