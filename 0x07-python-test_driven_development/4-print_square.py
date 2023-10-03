#!/usr/bin/python3

"""prints a square"""


def print_square(size):
    """confirms size -type and value and prints a square"""
    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        for j in range(size):
            print("#", end="")
        print()
