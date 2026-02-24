#!/usr/bin/python3
""""Class that inherits from list and prints the list sorted"""

class MyList(list):
    """This class inherits from list and has a public instance method that returns the list of available attributes and methods of the object"""

    def print_sorted(self):
        """This method prints the list in sorted order"""
        print(sorted(self))
