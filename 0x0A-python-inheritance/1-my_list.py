#!/usr/bin/python3

"""
    creates a child class from a parent class
"""


class MyList(list):
    """
        MyList class inherits from the class, list
        and therefore a sub or child class to the base
        or parent class
    """

    def print_sorted(self):
        """ print list in ascending order """
        new_list = sorted(self)
        print(new_list)
