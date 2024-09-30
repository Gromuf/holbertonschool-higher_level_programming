#!/usr/bin/python3
"""
This module defines a class Student that represents a student with
attributes for first name, last name, and age. It includes a method
to retrieve a dictionary representation of the student instance
for easy JSON serialization.
"""


class Student:
    """
    A class to define a student by their first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        Args:
            attrs (list, optional): A list of attribute names to retrieve.

        Returns:
            dict: A dictionary representation of the student.
        """
        if attrs is None:
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
            }
        json_dict = {}

        for attr in attrs:
            if hasattr(self, attr):
                json_dict[attr] = getattr(self, attr)
        return json_dict
