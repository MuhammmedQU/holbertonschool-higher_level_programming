#!/usr/bin/env python3
"""Module that contains the function inherits_from"""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class."""
    return issubclass(type(obj), a_class) and type(obj) != a_class

a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))
