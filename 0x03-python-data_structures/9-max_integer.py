#!/usr/bin/python3
def max_integer(my_list=[]):
    if (len(my_list) == 0):
        return None
    max = 0
    for idx in range(0, len(my_list)):
        if (my_list[idx] > max):
            max = my_list[idx]
    return max
