#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry(object):
    """Represent base geometry."""

    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        

class Rectangle(BaseGeometry):
    """Represent a rectangle."""

    def __init__(self, width, height):
        """Initialize a rectangle."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height 
