#!/usr/bin/python3

"""
    inserts a line of text to a file,
    after each line containing a specific string
    in a file
"""


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file """
    with open(filename, "r", encoding="utf-8") as this_file:
        read_lines = this_file.readlines()
        with open(filename, "w", encoding="utf-8") as this_file:
            for line in read_lines:
                this_file.write(line)
                if search_string in line:
                    this_file.write(new_string)
    """
    does not work yet:
    with open(filename, "a+", encoding="utf-8") as this_file:
        read_line = this_file.readline()
        if search_string in read_line:
            insert_point = f.tell()
            insert_text = new_string + '\n'
            this_file.write(insert_text[insert_point:])
    """
