#!/usr/bin/python3
"""
    function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """ finds the peak of a list of integers """
    if not list_of_integers:
        return None
    list_length = len(list_of_integers)
    if list_length == 1:
        return list_of_integers[0]
    elif list_length == 2:
        return max(list_of_integers)

    mid = int(list_length / 2)
    peak = list_of_integers[mid]
    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak
    elif peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
