#!/usr/bin/python3

"""
    unit tests for Square class
"""

import io
import unittest
import unittest.mock
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """
        tests cases for the properties and methods
        of the square class
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
        self.assertIsInstance(s1, Square)

    def test_init_width_varied_args(self):
        """
            initializes instances of a Square class
            with variable number of arguments
        """
        s2 = Square(7)
        self.assertEqual(s2.width, 7)
        self.assertEqual(s2.height, 7)
        self.assertEqual(s2.x, 0)
        self.assertEqual(s2.y, 0)
        self.assertEqual(s2.area(), 49)

        s3 = Square(5, 6, 7)
        self.assertEqual(s3.width, 5)
        self.assertEqual(s3.height, 5)
        self.assertEqual(s3.x, 6)
        self.assertEqual(s3.y, 7)
        self.assertEqual(s3.area(), 25)

        s4 = Square(5, 6, 7, 8)
        self.assertEqual(s4.width, 5)
        self.assertEqual(s4.height, 5)
        self.assertEqual(s4.x, 6)
        self.assertEqual(s4.y, 7)
        self.assertEqual(s4.area(), 25)
        self.assertEqual(s4.id, 8)

        s5 = Square(3, 2, id=-5)
        self.assertEqual(s5.id, -5)
        self.assertEqual(s5.area(), 9)
        self.assertIsInstance(s5, Square)

    def test_init_no_args(self):
        """ no args passed to class instantiation """
        with self.assertRaises(TypeError):
            Square()

    def test_init_neg_values(self):
        """ negative value passed as size """
        with self.assertRaises(ValueError):
            Square(-7)

        """ negative value passed to x """
        with self.assertRaises(ValueError):
            Square(3, -3, 2)

        """ negative value passed to y """
        with self.assertRaises(ValueError):
            Square(2, 3, -2)

    def test_init_zero_values(self):
        """ zero passed as argument """
        with self.assertRaises(ValueError):
            Square(0, 3, 2)

    def test_init_non_integer_values(self):
        """
            pass non integer values as arguments
        """
        with self.assertRaises(TypeError):
            Square("3")

        with self.assertRaises(TypeError):
            Square(3, "7", 5)

        with self.assertRaises(TypeError):
            Square(3, 7, "v", 2)

    def test_too_many_args(self):
        """
            too many arguments passed:
            TypeError: __init__() takes from 3 to 5 positional arguments
            but 6 were given
        """
        with self.assertRaises(TypeError):
            Square(3, 4, 5, 6, 7, 8)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, size, x, y, expected_output, mock_output):
        s = Square(size, x, y)
        s.display()
        self.assertEqual(mock_output.getvalue(), expected_output)

    def test_display(self):
        """
            test cases for the display method
        """
        self.assert_stdout(3, 0, 0, "###\n###\n###\n")
        self.assert_stdout(4, 2, 3,
                           "\n\n\n  ####\n  ####\n  ####\n  ####\n")


class TestSquare2(unittest.TestCase):
    """
        testing using the setUp and tearDown methods
    """

    def setUp(self):
        """
            sets up requirements for execution of
            following test cases
        """
        self.s6 = Square(4, 2, 1, 35)
        self.s7 = Square(10, 5, 8, 40)

    def test_area(self):
        """ test case for square area """
        self.assertEqual(self.s6.area(), 16)

    def test_set_size(self):
        """ tests set method for width """
        self.s6.size = 13
        self.assertEqual(self.s6.width, 13)
        self.assertEqual(self.s6.height, 13)

        """ test width non integers """
        with self.assertRaises(TypeError):
            self.s6.size = "4"

        """ test with negative values """
        with self.assertRaises(ValueError):
            self.s6.size = -5

        """ test with zero """
        with self.assertRaises(ValueError):
            self.s6.size = 0

    def test_set_x_and_y(self):
        """ tests set method for width """
        self.s6.x = 9
        self.s6.y = 10
        self.assertEqual(self.s6.x, 9)
        self.assertEqual(self.s6.y, 10)

        """ test width non integers """
        with self.assertRaises(TypeError):
            self.s6.x = "4"

        with self.assertRaises(TypeError):
            self.s6.y = "m"

        """ test with negative integers """
        with self.assertRaises(ValueError):
            self.s6.x = -4

        with self.assertRaises(ValueError):
            self.s6.y = -2

    def test__str__(self):
        """
            test case for __str__ method
        """
        self.assertEqual(self.s6.__str__(), "[Square] (35) 2/1 - 4")

    def test_to_dictionary(self):
        """
            test case for to_dictionary method
        """
        self.assertEqual(self.s6.to_dictionary(),
                         {"id": 35, "size": 4, "x": 2, "y": 1})

    def test_update(self):
        """ test for the update method """
        self.s6.update(100, 9, 4, 5)
        self.assertEqual(self.s6.__str__(), "[Square] (100) 4/5 - 9")

        self.s6.update(x=1, y=2, size=14)
        self.assertEqual(self.s6.__str__(), "[Square] (100) 1/2 - 14")

    def test_to_json_string(self):
        """ test case for conversion of dict object to json string """
        dictionary = self.s6.to_dictionary()
        self.assertEqual(Base.to_json_string([dictionary]),
                         '[{"id": 35, "size": 4, '
                         '"x": 2, "y": 1}]')

    def test_save_to_file(self):
        """ test case - writes json string representation to file """
        Square.save_to_file([self.s6, self.s7])
        with open("Square.json", "r") as files:
            self.assertEqual(files.read(),
                             '[{"id": 35, "size": 4, "x": 2, "y": 1}, '
                             '{"id": 40, "size": 10, "x": 5, "y": 8}]')
