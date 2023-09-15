#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary is None or a_dictionary == {}):
        return None
    sorted_dict = sorted(a_dictionary.items(), key=lambda item: item[1])
    max_value = sorted_dict.pop()
    return (max_value)
