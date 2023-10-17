#!/usr/bin/python3

"""
    unit tests for Square class
"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
        tests cases for the properties and methods
        of the Sqaure class
    """

    def test_init_all_args(self):
        """
            tests the initialization function of Square
        """
        s1 = Square(10, 3, 4, 12)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 4)
        self.assertEqual(s1.id, 12)
        self.assertEqual(s1.area(), 100)

    """
    def test_to_dictionary(self):
        returns dict format of square object
        s1 = Square(10, 3, 4, 22)
        self.assertEqual(s1.to_dictionary,
        {"id": 22, "size": 10, "x": 3, "y": 4})
    """

    def test_init_no_args(self):
        """ no args passed to class instantiation """
        with self.assertRaises(TypeError):
            Square()

    def test_init_neg_values(self):
        """ negative values passed as args of width and height """
        with self.assertRaises(ValueError):
            Square(-7)

        """ negative values passed to x and y """
        with self.assertRaises(ValueError):
            Square(3, -3, -2)
