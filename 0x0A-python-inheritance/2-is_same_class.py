#!/usr/bin/python3

"""
    Checks if an object is an instance of the specified class
"""


def is_same_class(obj, a_class):
    """
        compares obj with a_class and returns true
        if right else false
    """
    return isinstance(obj, a_class)
