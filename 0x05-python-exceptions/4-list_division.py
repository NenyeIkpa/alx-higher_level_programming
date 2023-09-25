#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = [0] * list_length

    for a in range(list_length):
        result = 0
        try:
            result = my_list_1[a] / my_list_2[a]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("index out of range")
        finally:
            new_list[a] = result
    return new_list
