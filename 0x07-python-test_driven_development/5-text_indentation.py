#!/usr/bin/python3

""" Conditional indentation of texts"""


def text_indentation(text):
    """text indentation"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    skip = 0

    for i in range(len(text)):
        if text[i] != " " or (i > 0 and text[i - 1] != " "):
            if text[i] == "." or text[i] == "?" or text[i] == ":":
                print(text[i], end="\n\n")
                skip = 1
            elif (text[i] == " " or text[i] == "\t") and skip == 1:
                pass
            else:
                print(text[i], end="")
                skip = 0
