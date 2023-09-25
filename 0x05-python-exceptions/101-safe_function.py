#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(args)
    except (Exception):
        result = None
        sys.stderr.write(Exception)
    finally:
        return result
