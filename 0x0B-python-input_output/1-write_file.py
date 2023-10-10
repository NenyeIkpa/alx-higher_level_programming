#!/usr/bin/python3

"""
    Writes a string to a textfile
"""


def write_file(filename="", text=""):
    """ replaces the existing contents of a text file with 'text' """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
