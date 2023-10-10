#!/usr/bin/python3

"""
    converts an object to its JSON representation
"""
import json


def to_json_string(my_obj):
    """ returns the JSON value of my_obj """
    return json.dumps(my_obj)
