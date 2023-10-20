#!/usr/bin/python3

"""
    Base class module
"""
import json
import csv


class Base:
    """ manages the id attribute """

    __nb_objects = 0

    def __init__(self, id=None):
        """ initializes the base class with its attributes """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ converts list of dictionaries to a json string """
        if not list_dictionaries:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save the contents in list_objs to file """
        if not list_objs:
            return []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            js = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
            f.write(js)

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of JSON string representation """
        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        # Create a dummy instance with a mandatory attribute (id)
        dummy_instance = cls(1, 1, 0, 0)

        if cls.__name__ == "Rectangle":
            if "width" in dictionary:
                dummy_instance.update(width=dictionary["width"])
            if "height" in dictionary:
                dummy_instance.update(height=dictionary["height"])
        elif cls.__name__ == "Square":
            if "size" in dictionary:
                dummy_instance.update(size=dictionary["size"])

        return dummy_instance

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ saves to csv file """
        if not list_objs:
            return []
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csv_file:
            fieldnames = list_objs[0].keys
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for row in list_objs:
                writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """ loads data from csv file """
        data = []
        filename = cls.__name__ + ".csv"
        with open(filename, mode="r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)
        print(data)
