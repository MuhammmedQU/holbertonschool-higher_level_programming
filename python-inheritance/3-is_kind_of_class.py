#!/usr/bin/python3
"""Class that inherits from another class"""

def is_kind_of_class(obj, a_class):
    """Returns True if the object is exactly an instance of the specified class ; otherwise False."""
    return  isinstance(obj, a_class)
