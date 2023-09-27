#!/usr/bin/python3
"""Creates a class named Square with attributes"""


class Square:
    """attributes include a private field; size and an init method"""

    def __init__(self, size=0, position=(0, 0)):
        """initialization functioni"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        if (len(position) != 2 or not isinstance(position[0], int) or not
                isinstance(position[1], int) or
                position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
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
        """set method for __position attribute"""
        if (len(value) != 2 or not isinstance(value[0], int) or not
                isinstance(value[1], int) or value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ calculates the area of a given square"""
        return self.__size ** 2

    def my_print(self):
        """prints a square of size, size"""
        if self.__size == 0:
            print()
        else:
            for x in range(0, self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__size):
                    if j == 0:
                        for k in range(self.__position[0]):
                            print(" ", end="")
                    print("#", end="")
                print()

    def __str__(self):
        """ i ain't sure what is going on here"""
        result = ""
        for q in range(self.__position[1]):
            result += "\n"
        for i in range(self.__size):
            result += " " * self.__position[0]
            result += "#" * self.__size
            if i < self.__size - 1:
                result += "\n"
        return result
