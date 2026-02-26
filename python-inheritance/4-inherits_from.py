#!/usr/bin/python3
"""Module that contains the function inherits_from"""


def inherits_from(obj, a_class):
    """Returns True if the object inherited from a_class."""
    return issubclass(type(obj), a_class) and type(obj) != a_class
