#!/usr/bin/python3

""" Say my name """


def say_my_name(first_name, last_name=""):
    """confirm parameters are strings and print name"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
