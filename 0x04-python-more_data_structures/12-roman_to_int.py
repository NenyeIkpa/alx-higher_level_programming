#!/usr/bin/python3
def get_roman_figure(c, p):
    if (p == 'I' and c == 'V'):
        return 3
    elif (p == 'I' and c == 'X'):
        return 8
    elif (p == 'X' and c == 'L'):
        return 30
    elif (p == 'X' and c == 'C'):
        return 80
    elif (p == 'C' and c == 'D'):
        return 300
    elif (p == 'C' and c == 'M'):
        return 800
    else:
        return get_roman_figure_2(c)


def get_roman_figure_2(c):
    if (c == 'I'):
        return 1
    elif (c == 'V'):
        return 5
    elif (c == 'X'):
        return 10
    elif (c == 'L'):
        return 50
    elif (c == 'C'):
        return 100
    elif (c == 'D'):
        return 500
    elif (c == 'M'):
        return 1000
    else:
        return 0


def roman_to_int(roman_string):
    if ((isinstance(roman_string, str) is False) or (roman_string is None)):
        return 0
    total = 0
    string_length = len(roman_string)
    total += get_roman_figure_2(roman_string[0])
    for idx in range(1, string_length):
        total = (total +
                 get_roman_figure(roman_string[idx], roman_string[idx - 1]))
    return total
