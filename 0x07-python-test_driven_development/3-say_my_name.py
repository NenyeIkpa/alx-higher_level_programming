#!/usr/bin/python3

""" Say my name """


def say_my_name(first_name="", last_name=""):
    """confirm parameters are strings and print name"""
    if not isinstance(first_name, str) or type(first_name) is None:
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str) or type(last_name) is None:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
