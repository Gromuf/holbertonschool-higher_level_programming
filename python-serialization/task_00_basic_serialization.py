#!/usr/bin/env python3
"""
This module provides functions for serializing a Python dictionary into
a JSON file and deserializing the JSON file to recreate the dictionary.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize the Python dictionary `data` into JSON format and save it to
    the specified file `filename`. If the file already exists, it will be
    replaced.

    Parameters:
    data (dict): The dictionary to serialize and save.
    filename (str): The path of the file where the JSON data will be saved.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Load JSON data from the specified file `filename` and deserialize it into
    a Python dictionary.

    Parameters:
    filename (str): The path of the file to load the JSON data from.

    Returns:
    dict: The deserialized Python dictionary from the JSON file.
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
