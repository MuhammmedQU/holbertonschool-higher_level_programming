#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for key, value in sorted(a_dictionary.items()):
        print(f"{key}: {value}")


def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary
