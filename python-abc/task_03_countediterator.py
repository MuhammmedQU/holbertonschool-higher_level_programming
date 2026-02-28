#!/usr/bin/python3
"""Module that defines the CountedIterator class"""


class CountedIterator:
    """Iterator that keeps track of the number of iterated items"""

    def __init__(self, data):
        """Initialize iterator and counter"""
        self.data = iter(data)
        self.count = 0

    def __iter__(self):
        """Return the iterator object itself"""
        return self

    def __next__(self):
        """Return next item and increment counter"""
        value = next(self.data)
        self.count += 1
        return value

    def get_count(self):
        """Return number of iterated items"""
        return self.count
