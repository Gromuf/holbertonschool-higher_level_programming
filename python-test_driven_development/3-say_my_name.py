#!/usr/bin/python3

"""
3-say_my_name

This module provides a function to print a formatted string with a first name
and an optional last name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first_name> <last_name>".

    Parameters:
    first_name (str): The first name to be printed.
    last_name (str, optional): The last name to be printed.

    Raises:
    TypeError: If first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
