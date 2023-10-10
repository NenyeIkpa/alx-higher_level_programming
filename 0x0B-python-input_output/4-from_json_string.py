#!/usr/bin/python3

"""
    converts a JSON string to its object
"""
import json


def from_json_string(my_str):
    """ returns object represented by JSON string, my_str """
    return json.loads(my_str)
