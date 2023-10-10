#!/usr/bin/python3

"""
    Appends a string to a textfile
"""


def append_write(filename="", text=""):
    """ append a string to the existing contents of a text file """
    appended = 0
    with open(filename, "a", encoding="utf-8") as f:
        appended = f.write(text)
    return appended
