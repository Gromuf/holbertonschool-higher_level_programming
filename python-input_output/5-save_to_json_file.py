#!/usr/bin/python3
"""
This module provides a function to save an object to a text file
in JSON format using the built-in `json` library.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj: The object to be serialized to JSON.
        filename (str): The name of the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
