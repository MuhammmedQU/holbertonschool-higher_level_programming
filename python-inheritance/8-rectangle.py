#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class Rectangle(BaseGeometry):
    """Represent a rectangle."""

    def __init__(self, width, height):
        """Initialize a rectangle."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height 
