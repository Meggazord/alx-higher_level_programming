#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    result = 0
    for item in my_list:
        if item not in new_list:
            new_list.append(item)
    for item in new_list:
        result += item
    return result
