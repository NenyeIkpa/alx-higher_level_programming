#!/usr/bin/python3

""" Conditional indentation of texts"""


def text_indentation(text):
    """text indentation"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    skip = 0

    for char in text:
        if char == "." or char == "," or char == "?" or char == ":":
            print(char, end="\n\n")
            skip = 1
        elif (char == " " or char == "\t") and skip == 1:
            pass
        else:
            print(char, end="")
            skip = 0
