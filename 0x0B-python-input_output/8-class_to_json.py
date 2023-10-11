#!/usr/bin/python3

"""
    Creates the dictionary description for JSON serialization
    of the attributes of an object
"""


def class_to_json(obj):
    """
        returns a dictionary with the whose key is the
        attributes of an object anf values, the JSON serialized
        format
    """

    serialized = {}
    attributes = dir(obj)
    for attribute in attributes:
        if not attribute.startswith('_'):
            value = getattr(obj, attribute)
            """
                check if value is of a serializable type
                add to dictionary if so
            """
            if isinstance(value, (int, str, list, dict, bool)):
                serialized[attribute] = value
    return serialized
