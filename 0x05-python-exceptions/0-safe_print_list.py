#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    if (my_list == []):
        return 0
    for i in range(x):
        try:
            count += 1
            print("{}".format(my_list[i]), end="" if i < x - 1 else "\n")
        except IndexError:
            print()
            return count - 1
    return count
