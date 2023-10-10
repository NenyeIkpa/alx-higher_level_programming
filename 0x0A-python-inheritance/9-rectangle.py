#!/usr/bin/python3

"""
    creates a rectangle class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class rectangle inherit from BaseGeomtery class """

    def __init__(self, width, height):
        """ initializes the rectangle class """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ returns the area of a rectangle """
        return self.__width * self.__height

    def __str__(self):
        """returns a string formatted output """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
