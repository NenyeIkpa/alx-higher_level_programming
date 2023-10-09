#!/usr/bin/python3

"""
    Returns True if the object is an instance of, or if the object
    is an instance of a class that inherited from, the specified class
"""


def is_kind_of_class(obj, a_class):
    """ As described above """
    return isinstance(obj, a_class)
