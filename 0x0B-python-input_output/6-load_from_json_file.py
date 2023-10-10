#!/usr/bin/python3

"""
    creates an object from a JSON file
"""
import json


def load_from_json_file(filename):
    """ reads the JSON file,filename, and creates an object from it """
    with open(filename, "r", encoding="utf-8") as the_file:
        return json.load(the_file)
