#!/usr/bin/python3

"""
    creates a class
"""


class BaseGeometry:
    """ a class named BaseGeometry """
    def area(self):
        """ raises an exception """
        return Exception("area() is not implemented")
