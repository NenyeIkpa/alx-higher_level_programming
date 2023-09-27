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
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ calculates the area of a given square"""
        return self.__size ** 2

    def my_print(self):
        """prints a square of size, size"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
