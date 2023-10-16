#!/usr/bin/python3

"""
    square module
    inerits from rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ blueprint of a square """
    def __init__(self, size, x=0, y=0, id=None):
        """
            initializes an instance of a square
            using the methods of the super class
        """
        super().__init__(size, size, x, y, id)

    @property
    def size:
        """ get method for size attribute  """
        return self.__width

    @size.setter
    def size(self, value):
        """ set method for size attribute """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = size

    def __str__(self):
        """ returns a string representation of class attributes """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)
