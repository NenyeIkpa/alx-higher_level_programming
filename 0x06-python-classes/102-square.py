#!/usr/bin/python3
"""Creates a class named Square with attributes"""


class Square:
    """attributes include a private field; size and an init method"""

    def __init__(self, size=0):
        """initialization function"""
        self.__size = size

    @property
    def size(self):
        """ get method for private attribute __size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set method for __size attribute"""
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ calculates the area of a given square"""
        return self.__size ** 2

    def __eq__(self, other):
        """equality check between object instances"""
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """not equal to check"""
        if isinstance(other, Square):
            return self.area() != other.area()
        return True

    def __gt__(self, other):
        """greater than check"""
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """greater than or equal to check"""
        if isinstance(other, Square):
            return self.area() >= other.area()
        return False

    def __lt__(self, other):
        """less than check"""
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """less than or equal to check"""
        if isinstance(other, Square):
            return self.area() <= other.area()
        return False
