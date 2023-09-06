#!/usr/bin/python3
for letter in range(ord('z'), ord('a') - 1, -1):
    if (letter % 2 == 0):
        num = 0
    else:
        num = 32
    print("{}".format(chr(letter - num)), end="")
