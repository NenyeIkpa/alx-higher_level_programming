#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    message = "Exception: Unknown format code 'd' for object of type 'str'\n"
    try:
        print("{:d}".format(int(value)))
        return True
    except (Exception):
        sys.stderr.write(message)
        return False
