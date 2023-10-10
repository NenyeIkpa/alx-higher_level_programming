#!/usr/bin/python3

"""
    verifies if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """ returns true if obj is a subclass of a """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
