#!/usr/bin/python3
print_reversed_list_integer = (__import__('3-print_reversed_list_integer').
                               print_reversed_list_integer)

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)
print("-------------------------")
my_list = [1]
print_reversed_list_integer(my_list)
print("-------------------------")
my_list = [0]
print_reversed_list_integer(my_list)
print("-------------------------")
my_list = [-10, -9, 7, 8, -1]
print_reversed_list_integer(my_list)
print("-------------------------")
my_list = []
print_reversed_list_integer(my_list)
print("-------------------------")
my_list = [6, 7, 8, 9, 10]
print_reversed_list_integer(my_list)

