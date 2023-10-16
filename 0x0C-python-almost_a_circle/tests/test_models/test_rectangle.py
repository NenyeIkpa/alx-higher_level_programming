#!/usr/bin/python3

"""
    unit tests for Rectangle class
"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
        tests cases for the properties and methods
        of the rectangle class
    """

    def test_init_all_args(self):
        """
            tests the initialization function of Rectangle
        """
        r1 = Rectangle(10, 5, 3, 4, 12)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, 12)
        self.assertEqual(r1.area(), 50)

    def test_init_no_args(self):
        """ no args passed to class instantiation """
        with self.assertRaises(TypeError):
            Rectangle()

    def test_init_neg_values(self):
        """ negative values passed as args of width and height """
        with self.assertRaises(ValueError):
            Rectangle(-7, -3)

        """ negative values passed to x and y """
        with self.assertRaises(ValueError):
            Rectangle(2, 3, -3, -2)
