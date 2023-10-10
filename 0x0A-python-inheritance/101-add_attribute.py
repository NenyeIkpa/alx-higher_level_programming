#!/usr/bin/python3

"""
    adds a new attribute to an object, if possible
"""

def add_attribute(obj, name, value):
    """ sets a new attibute to an object if arguments are as required """
    if name is None or len(name) <= 0 or value is None:
         raise TypeError("can't add new attribute")
    if not hasattr(obj, name ):
        setattr(obj, name, value)
