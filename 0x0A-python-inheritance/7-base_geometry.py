#!/usr/bin/python3

"""
    creates a class
"""


class BaseGeometry:
    """ a class named BaseGeometry """
    def area(self):
        """ raises an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates the status of the variable value
            reaises an exception when value is not an integer
            or its value is <= 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
