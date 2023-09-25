#!/usr/bin/python3

def safe_function(fct, *args):
    try:
        print("{:d}".format(fct(int(args))))
        return True
    except (Exception):
        Exception("Unknown format code 'd' for object of type 'str'")
        return False
