#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    arglen = len(argv)
    idx = 0
    if (arglen == 1):
        print("0 arguments.")
    else:
        word = "argument" if arglen == 2 else "arguments"
        print("{} {}:".format(arglen - 1, word))
        for arg in argv:
            if (idx != 0):
                print("{}: {}".format(idx, arg))
            idx += 1
