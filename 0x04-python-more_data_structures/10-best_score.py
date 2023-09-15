#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary == None):
        return None
    sorted_dict = sorted(a_dictionary)
    last_idx = sorted_dict.popItem()
    print(last_idx)
    return(last_idx)
