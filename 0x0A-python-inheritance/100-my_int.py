#!/usr/bin/python3

"""
    Creates MyInt class
"""


class MyInt(int):
    """ inherit all the properties of int class """

    def __eq__(self, other):
        """equality check between object instances"""
        if isinstance(other, MyInt):
            return self.__int != other.__int()
        return False

    def __ne__(self, other):
        """not equal to check"""
        if isinstance(other, MyInt):
            return self.__int == other.__int
        return True
