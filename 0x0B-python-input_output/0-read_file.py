#!/usr/bin/python3

"""
    Reads a textfile and prints out its contents
 """


def read_file(filename=""):
    """
        opens a file,
        reads its contents and
        prints the contents to standard output
    """
    with open(filename, encoding="utf-8") as f:
        fread = f.read()
        print(fread, end="")
