#!/usr/bin/python3
"""Module for integer addition"""

def add_integer(a, b=98):
    """Adds two integers and returns their sum"""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        if a != a or a in (float("inf"), float("-inf")):
            raise TypeError("a must be an integer")
        a = int(a)

    if isinstance(b, float):
        if b != b or b in (float("inf"), float("-inf")):
            raise TypeError("b must be an integer")
        b = int(b)

    return a + b
