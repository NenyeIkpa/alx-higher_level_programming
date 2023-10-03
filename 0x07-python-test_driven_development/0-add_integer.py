#!/usr/bin/python3
""" Calculates the sum of two numbers
    numbers can be of type int or float
    otherwise, program will raise a TypeError
"""

def add_integer(a, b=98):
    """checks if  a and b are of type int or float,
    returns sum of a and b if true
    else raises TypeError"""
    if type(a) not in [int, float] or type(a) is None:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
