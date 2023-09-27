#!/usr/bin/python3
"""Creates a class named Square with attributes"""


class Square:
    """attributes include a private field; size and an init method"""

    def __init__(self, size=0, position=(0, 0)):
        """initialization function"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ get method for private attribute __size"""
        return self.__size

    @property
    def position(self):
        """returns the position of given square"""
        return self.__position

    @size.setter
    def size(self, value):
        """set method for __size attribute"""
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        if type(value) is not int or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self__position = position

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
                    if j == 0:
                        for k in range(self.__position[0]):
                            print(" ", end="")
                    print("#", end="")
                print()
