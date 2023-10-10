#!/usr/bin/python3

"""
    Appends a string to a textfile
"""


def append_write(filename="", text=""):
    """ append a string to the existing contents of a text file """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
