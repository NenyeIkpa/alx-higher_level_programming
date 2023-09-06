#!/usr/bin/python
def uppercase(str):
    new_str = ""

    for char in str:
        for i in range(ord('a'), ord('z') + 1):
            if (ord(char) == i):
                new_char = chr(i - 32)
                new_str += new_char
            else:
                new_char = char
    print(new_str)
