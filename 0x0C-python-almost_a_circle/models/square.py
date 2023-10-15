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

    def __str__(self):
        """ returns a string representation of class attributes """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)
