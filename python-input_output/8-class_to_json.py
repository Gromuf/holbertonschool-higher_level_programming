#!/usr/bin/python3
"""
This module provides a function to return the dictionary description
of an object for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.

    Args:
        obj: An instance of a Class.

    Returns:
        dict: A dictionary representation of the object.
    """
    json_dict = {}

    for attribute, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[attribute] = value
    return json_dict
