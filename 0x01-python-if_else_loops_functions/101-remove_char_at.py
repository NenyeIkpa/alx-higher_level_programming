#!/usr/bin/python3
def remove_char_at(str, n):
    idx = 0
    output = ""
    for char in str:
        if (idx != n):
            output += char
        idx += 1
    return output
