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

    def test_init_width_varied_args(self):
        """
            initializes instances of a Rectangle class
            with variable number of arguments
        """
        r2 = Rectangle(2, 7)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 7)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r2.area(), 14)

        r3 = Rectangle(5, 6, 7)
        self.assertEqual(r3.width, 5)
        self.assertEqual(r3.height, 6)
        self.assertEqual(r3.x, 7)
        self.assertEqual(r3.y, 0)
        self.assertEqual(r3.area(), 30)

        r4 = Rectangle(5, 6, 7, 8)
        self.assertEqual(r4.width, 5)
        self.assertEqual(r4.height, 6)
        self.assertEqual(r4.x, 7)
        self.assertEqual(r4.y, 8)
        self.assertEqual(r4.area(), 30)

        r5 = Rectangle(3, 2, id=-5)
        self.assertEqual(r5.id, -5)

        r6 = Rectangle(4, 6, 2, 1, 33)
        self.assertEqual(r6.__str__(), "[Rectangle] (33) 2/1 - 4/6")
        self.assertEqual(r6.to_dictionary(),
                         {"id": 33, "width": 4, "height": 6, "x": 2, "y": 1})

    def test_init_no_args(self):
        """ no args passed to class instantiation """
        with self.assertRaises(TypeError):
            Rectangle()

    def test_init_neg_values(self):
        """ negative value passed as width """
        with self.assertRaises(ValueError):
            Rectangle(-7, 3)

        """ negative value passed as height """
        with self.assertRaises(ValueError):
            Rectangle(7, -3)

        """ negative value passed to x """
        with self.assertRaises(ValueError):
            Rectangle(2, 3, -3, 2)

        """ negative value passed to y """
        with self.assertRaises(ValueError):
            Rectangle(2, 3, 3, -2)

    def test_init_zero_values(self):
        """ zero passed as argument """
        with self.assertRaises(ValueError):
            Rectangle(0, 3)

        with self.assertRaises(ValueError):
            Rectangle(7, 0)

    def test_init_non_integer_values(self):
        """
            pass non integer values as arguments
        """
        with self.assertRaises(TypeError):
            Rectangle("3", 7)

        with self.assertRaises(TypeError):
            Rectangle(3, "7")

        with self.assertRaises(TypeError):
            Rectangle(3, 7, "v", 2)

        with self.assertRaises(TypeError):
            Rectangle(3, 7, 2, "8")
