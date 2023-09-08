#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    for idx in range(0, len(new_list)):
        num = new_list[idx]
        if (num % 2 != 0):
            num = 0
    return new_list
