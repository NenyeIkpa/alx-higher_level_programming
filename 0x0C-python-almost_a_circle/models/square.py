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
    def size(self):
        """ get method for size attribute  """
        return self.width

    @size.setter
    def size(self, value):
        """ set method for size attribute """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def __str__(self):
        """ returns a string representation of class attributes """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """
            updates class attribute using
            no-keyword argument
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                if type(args[1]) is not int:
                    raise TypeError("width must be an integer")
                if args[1] <= 0:
                    raise ValueError("width must be > 0")
                self.__width = args[1]
                self.__height = args[1]
            if len(args) >= 3:
                if type(args[2]) is not int:
                    raise TypeError("x must be an integer")
                if args[2] < 0:
                    raise ValueError("x must be >= 0")
                self.__x = args[2]
            if len(args) >= 4:
                if type(args[3]) is not int:
                    raise TypeError("y must be an integer")
                if args[3] < 0:
                    raise ValueError("y must be >= 0")
                self.__y = args[3]
        else:
            arg_list = ["id", "width", "x", "y"]
            for key, value in kwargs.items():
                if key == arg_list[0]:
                    self.__id = value
                if key == arg_list[1]:
                    if type(value) is not int:
                        raise TypeError("width must be an integer")
                    if value <= 0:
                        raise ValueError("width must be > 0")
                    self.__width = value
                    self.__height = value
                if key == arg_list[2]:
                    if type(value) is not int:
                        raise TypeError("x must be an integer")
                    if value < 0:
                        raise ValueError("x must be >= 0")
                    self.__x = value
                if key == arg_list[3]:
                    if type(value) is not int:
                        raise TypeError("y must be an integer")
                    if value < 0:
                        raise ValueError("y must be >= 0")
                    self.__y = value

        def to_dictionary(self):
            """ returns dict representation of a square """
            return self.__dict__
