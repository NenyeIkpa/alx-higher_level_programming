#!/usr/bin/python3

"""
    script that adds all arguments to a Python list,
    and then save them to a file
"""
import sys
import os

""" import required files """
save_to = __import__('5-save_to_json_file').save_to_json_file
load_from = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

"""
    check if filename already exists and
    load its contents to the python list, my list
"""
if os.path.exists(filename):
    mylist = load_from(filename)
else:
    mylist = []

""" when command line args are available, append them to the python list """
for arg in sys.argv[1:]:
    mylist.append(arg)
save_to(mylist, filename)
