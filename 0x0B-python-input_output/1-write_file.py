#!/usr/bin/python3

"""
    Writes a string to a textfile
"""


def write_file(filename="", text=""):
    """ replaces the existing contents of a text file with 'text' """
    written = 0
    with open(filename, "w", encoding="utf-8") as f:
        written = f.write(text)
    return written
