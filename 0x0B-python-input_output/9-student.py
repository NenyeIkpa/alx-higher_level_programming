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

    def to_json(self):
        """ returns a dict of serialized JSON student """
        serialized_student = {}
        serialized_student["first_name"] = self.first_name
        serialized_student["last_name"] = self.last_name
        serialized_student["age"] = self.age
        return serialized_student
