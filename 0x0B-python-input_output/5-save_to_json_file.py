#!/usr/bin/python3

"""
    writes an object to a text file using JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """ writes the contents of my_obj to filename using JSON format """
    with open(filename, "w", encoding="utf-8") as a_file:
        return json.dump(my_obj, a_file)
