#!/usr/bin/python3

"""
    unit tests for Base class
"""


import unittest

from models.base import Base


class TestBase(unittest.TestCase):
    """
        holds all the test cases for the Base class
    """
    def test_init(self):
        """
            tests cases for attributes and methods of the base class
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base(10)
        self.assertEqual(b2.id, 10)

        b3 = Base()
        self.assertEqual(b3.id, 2)

        b4 = Base(-5)
        self.assertEqual(b4.id, -5)
        self.assertIsInstance(b4, Base)

        b5 = Base(100)
        self.assertEqual(b5.id, 100)
        self.assertIsInstance(b5, Base)

    if __name__ == "__main__":
        unittest.main()
