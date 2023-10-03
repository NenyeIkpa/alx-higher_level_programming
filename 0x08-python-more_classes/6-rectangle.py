#!/usr/bin/python3
"""Defines a rectangle class"""


class Rectangle:
    """ holds all the properties of the Rectangle class"""

    # variables hold the number of rectangle objects created
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width

        # variable increased by 1, everytime a rectangle object is created
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """ printable string of an instance of a rectangle with #"""
        output = ""
        if self.__width == 0 or self.__height == 0:
            return output
        for _ in range(self.__height):
            end = "\n" if _ < self.__height - 1 else ""
            output += "#" * self.__width + end
        return output

    def __repr__(self):
        """ official representation of an instance of a rectangle with #"""
        return "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"

    def __del__(self):
        """rectangle deletion"""
        print("Bye rectangle...")

        # variable decreased by 1, anytime an instance is deleted
        Rectangle.number_of_instances -= 1
