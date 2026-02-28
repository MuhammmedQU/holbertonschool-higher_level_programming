#!/usr/bin/python3
"""Module that defines Shape abstract class and its subclasses"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes"""

    @abstractmethod
    def area(self):
        """Calculate area of the shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter of the shape"""
        pass


class Circle(Shape):
    """Circle shape"""

    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        """Return area of the circle"""
        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        """Return perimeter of the circle"""
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """Rectangle shape"""

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        """Return area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter of the rectangle"""
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    """Print area and perimeter of a shape (duck typing)"""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
