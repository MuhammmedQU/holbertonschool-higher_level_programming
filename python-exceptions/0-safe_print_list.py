#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if x < 0:
        return 0
    elif x > len(my_list):
        x = len(my_list)
    for i in range(x):
        print(my_list[i], end="")
    print()
    return x
