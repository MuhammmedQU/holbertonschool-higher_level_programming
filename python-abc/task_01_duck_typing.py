#!/usr/bin/python3
"""Module that defines an abstract class and its subclasses"""
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Abstract class that defines a shape"""

    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    


class Circle(Shape):

    def __init__(self, radius):
        self.__radius = radius
    
    def area(self):
        return math.pi * self.__radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.__radius
    

class Rectangle(Shape):

    def __init__(self, witdh, height):
        self.__witdh = witdh
        self.__height = height
    
    def area(self):
        return self.__witdh * self.__height
    
    def perimeter(self):
        return 2 * (self.__witdh + self.__height)    
    
    

def shape_info(shape):
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
