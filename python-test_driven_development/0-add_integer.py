#!/usr/bin/python3
"""Module for integer addition"""
import math


def add_integer(a, b=98):
    """Adds two integers and returns their sum"""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float) and not math.isfinite(a):
        raise TypeError("a must be an integer")
    if isinstance(b, float) and not math.isfinite(b):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
