#!/usr/bin/python3

"""
    creates a rectangle class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class rectangle inherit from BaseGeomtery class """

    def __init__(self, width, height):
        """ initializes the rectangle class """
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
