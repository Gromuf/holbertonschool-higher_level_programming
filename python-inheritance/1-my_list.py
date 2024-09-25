#!/usr/bin/python3
"""module for class my_list"""


class MyList(list):
    """
    A subclass of `list` with an additional method to print the list
    sorted in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.

        Assumes all elements in the list are integers.
        """
        print(sorted(self))
