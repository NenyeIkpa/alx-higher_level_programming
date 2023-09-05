#!/usr/bin/python3
def islower(c):
    for i in range(ord('a'), ord('z') + 1):
        if (c is chr(i)):
            return True
    return False
