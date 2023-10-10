#!/usr/bin/python3

"""
    Creates a square class
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ square class hhas a super class, Rectangle """

    def __init__(self, size):
        """ initializes square class """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ returns the area of a square """
        return self.__size ** 2

    def __str__(self):
        """return string formatted ouptut of square attributes """
        return "[Square] {}/{}".format(self.__size, self.__size)
