#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    arglen = len(argv)
    total = 0
    idx = 0
    if (arglen > 0):
        for arg in argv:
            if (idx > 0):
                total += int(arg)
            idx += 1
    print(total)
