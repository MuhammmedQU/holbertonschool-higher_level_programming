#!/usr/bin/env python3
"""Module that defines Fish, Bird and FlyingFish classes"""


class SwimMixin:

    def swim(self):
        """Method that prints a string"""
        print("The creature swims!")

class FlyMixin:

    def fly(self):
        """Method that prints a string"""
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """Class that inherits from SwimMixin and FlyMixin"""
    def roar(self):
        """Method that prints a string"""
        print("The dragon roars!")                
