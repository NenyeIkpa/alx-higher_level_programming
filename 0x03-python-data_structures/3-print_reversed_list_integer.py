#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """if isinstance(my_list, list):
        my_list.reverse()
        for num in my_list:
            print("{:d}".format(num))"""
    for i in range(len(my_list) - 1, -1, -1):
        if (i):
            print("{:d}".format(my_list[i]))
