#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for k, v in a_dictionary.items():
        a = k if type(k) is int else v
        new_dictionary[a] = a_dictionary[a] * 2
    return new_dictionary
