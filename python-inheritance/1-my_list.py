#!/usr/bin/python3
"""
This module defines a class `MyList` that inherits from the built-in `list`
class and adds a method to print the list sorted in ascending order.
"""


class MyList(list):
    """
    A subclass of `list` with an additional method to print the list sorted.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.

        Assumes all elements in the list are integers.
        """
        print(sorted(self))
