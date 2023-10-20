#!/usr/bin/python3

"""
    unit tests for Rectangle class
"""

import io
import unittest
import unittest.mock
from models.rectangle import Rectangle
from models.base import Base


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
        self.assertIsInstance(r1, Rectangle)

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
        self.assertEqual(r5.area(), 6)
        self.assertIsInstance(r5, Rectangle)

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

    def test_too_many_args(self):
        """
            too many arguments passed:
            TypeError: __init__() takes from 3 to 6 positional arguments
            but 7 were given
        """
        with self.assertRaises(TypeError):
            Rectangle(3, 4, 5, 6, 7, 8, 9)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, width, height, x, y, expected_output, mock_output):
        r = Rectangle(width, height, x, y)
        r.display()
        self.assertEqual(mock_output.getvalue(), expected_output)

    def test_display(self):
        """
            test cases for the display method
        """
        self.assert_stdout(7, 2, 0, 0,  "#######\n#######\n")
        self.assert_stdout(3, 6, 0, 0, "###\n###\n###\n###\n###\n###\n")
        self.assert_stdout(4, 4, 2, 3,
                           "\n\n\n  ####\n  ####\n  ####\n  ####\n")


class TestRectangle2(unittest.TestCase):
    """
        testing using the setUp and tearDown methods
    """

    def setUp(self):
        """
            sets up requirements for execution of
            following test cases
        """
        self.r6 = Rectangle(4, 6, 2, 1, 33)
        self.r7 = Rectangle(10, 7, 2, 8, 40)

    def test_area(self):
        """ test case for rectangle area """
        self.assertEqual(self.r6.area(), 24)

    def test__str__(self):
        """
            test case for __str__ method
        """
        self.assertEqual(self.r6.__str__(), "[Rectangle] (33) 2/1 - 4/6")

    def test_to_dictionary(self):
        """
            test case for to_dictionary method
        """
        self.assertEqual(self.r6.to_dictionary(),
                         {"id": 33, "width": 4, "height": 6, "x": 2, "y": 1})

    def test_update(self):
        """ test for the update method """
        self.r6.update(89, 2, 3, 4, 5)
        self.assertEqual(self.r6.__str__(), "[Rectangle] (89) 4/5 - 2/3")

        self.r6.update(x=1, height=2, y=3, width=4)
        self.assertEqual(self.r6.__str__(), "[Rectangle] (89) 1/3 - 4/2")

    def test_to_json_string(self):
        """ test case for conversion of dict object to json string """
        dictionary = self.r6.to_dictionary()
        self.assertEqual(Base.to_json_string([dictionary]),
                         '[{"id": 33, "width": 4, "height": 6, '
                         '"x": 2, "y": 1}]')

    def test_save_to_file(self):
        """ test case - writes json string representation to file """
        Rectangle.save_to_file([self.r6, self.r7])
        with open("Rectangle.json", "r") as files:
            self.assertEqual(files.read(),
                             '[{"id": 33, "width": 4, "height": 6, "x": 2, '
                             '"y": 1}, {"id": 40, "width": 10, '
                             '"height": 7, "x": 2, "y": 8}]')
