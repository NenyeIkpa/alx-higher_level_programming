#!/usr/bin/python3
"""Creates a class named Square with attributes"""


class Square:
    """attributes include a private field; size and an init method"""

    __size = None

    def __init__(self, size):
        """initialization function"""
        self.__size = size
