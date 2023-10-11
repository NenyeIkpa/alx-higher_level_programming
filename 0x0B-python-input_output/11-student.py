#!/usr/bin/python3

"""
    creates a Student class that includes a method
    for retrieving the dictionary representation of
    a student
"""


class Student:
    """ a student class with its own attributes """
    def __init__(self, first_name, last_name, age):
        """ initializes a student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ returns a dict of serialized JSON student """
        serialized_student = {}
        if attrs is None:
            # If attrs is not provided, retrieve all attributes
            return self.__dict__
        else:
            # If attrs is provided, retrieve only the specified attributes
            for attr in attrs:
                if hasattr(self, attr):
                    value = getattr(self, attr)
                    serialized_student[attr] = value
        return serialized_student
        """
            alternative, one liner implementation:
            return {attr: getattr(self, attr)
            for attr in attrs if hasattr(self, attr)}
        """
    def reload_from_json(self, json):
        """ replaces all attributes of the student instance """
        for key, value in json.items():
            setattr(self, key, value)
