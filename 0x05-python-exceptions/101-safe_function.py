#!/usr/bin/python3

def safe_function(fct, *args):
    try:
        return fct(args)
    except (Exception):
        Exception("Unknown format code 'd' for object of type 'str'")
        return 0
