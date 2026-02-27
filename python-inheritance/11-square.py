#!/usr/bin/python3
"""Defines a Square class."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def print(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
