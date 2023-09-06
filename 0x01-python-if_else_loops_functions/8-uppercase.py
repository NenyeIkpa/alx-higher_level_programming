#!/usr/bin/python3
def uppercase(str):
    new_str = ""

    for char in str:
        val = ord(char)
        if (val >= ord('a') and val <= ord('z')):
            new_char = chr(val - 32)
        else:
            new_char = char
        new_str += new_char
    print(new_str)
