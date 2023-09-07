#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    argv = sys.argv
    arglen = len(argv)

    if (arglen != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = argv[1]
        b = argv[3]
        operator = argv[2]
        if (operator == "+"):
            print("{} + {} = {}".format(a, b, add(int(a), int(b))))
        elif (operator == "-"):
            print("{} - {} = {}".format(a, b, sub(int(a), int(b))))
        elif (operator == "*"):
            print("{} * {} = {}".format(a, b, mul(int(a), int(b))))
        elif (operator == "/"):
            print("{} / {} = {}".format(a, b, div(int(a), int(b))))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
