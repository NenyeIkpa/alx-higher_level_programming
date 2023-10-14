#!usr/bin/python3

"""
    class Rectangle
"""

from models.base import Base


class Rectangle(Base):
    """ sets the blueprint of a rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
            initializes an instance of the rectangle class
            id = unique id of rectangle
            width = width of rectangle
            height = height of rectangle
            x = x co-ordinate position of rectangle
            y = y co-ordinate position of rectangle
        """
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ get method for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ set method for width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ get method for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set method for height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ get method for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ set method for x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ get method for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ set method for y """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ returns the area of a rectangle """
        return self.__width * self.__height

    def display(self):
        """ prints out the rectangle with symbol # """
        print("\n" * self.__y, end="")
        for h in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """ returns a string formatted output of a rectangle """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args):
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
                        raise ValueError("width must be >= 0")
                    self.__width = args[1]
                if len(args) >= 3:
                    if type(args[2]) is not int:
                        raise TypeError("height must be an integer")
                    if args[2] <= 0:
                        raise ValueError("height must be > 0")
                    self.__height = args[2]
                if len(args) >= 4:
                    if type(args[3]) is not int:
                        raise TypeError("x must be an integer")
                    if args[3] < 0:
                        raise ValueError("x must be > 0")
                    self.__x = args[3]
                if len(args) >= 5:
                    if type(args[4]) is not int:
                        raise TypeError("y must be an integer")
                    if args[4] < 0:
                        raise ValueError("y must be > 0")
                    self.__y = args[4]
