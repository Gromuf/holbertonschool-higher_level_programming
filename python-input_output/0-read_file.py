#!/usr/bin/python3
"""
This module defines a function to read and print a UTF-8 encoded text file.

The function `read_file` opens a specified text file in read mode,
reads its content, and prints it to stdout. The file is read using
UTF-8 encoding. The file is automatically closed after reading.

No exceptions for file permissions or missing files are handled.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its content to stdout.

    Args:
        filename (str): The name of the file to read.
                        If not provided, defaults to an empty string.

    Returns:
        None
    """
    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read(), end="")
