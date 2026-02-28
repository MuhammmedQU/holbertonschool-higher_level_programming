#!/usr/bin/python3
"""Module that defines Shape abstract class and its subclasses"""

from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class for shapes"""

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Circle shape"""

    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return 3.141592653589793 * (self.__radius ** 2)

    def perimeter(self):
        return 2 * 3.141592653589793 * self.__radius


class Rectangle(Shape):
    """Rectangle shape"""

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
