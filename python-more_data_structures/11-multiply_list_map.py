#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    for i in range(len(my_list)):
        my_list[i] *= number
    return my_list
