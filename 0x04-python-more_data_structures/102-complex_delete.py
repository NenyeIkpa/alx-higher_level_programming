#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_del_list = []
    for k, v in a_dictionary.items():
        if (v == value):
            key_del_list.append(k)
    for key in key_del_list:
        del a_dictionary[key]
    return a_dictionary
