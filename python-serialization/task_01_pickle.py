#!/usr/bin/env python3
"""
This module defines a custom class `CustomObject` that supports serialization
and deserialization using the pickle module.
"""
import pickle


class CustomObject:
    """
    A custom Python object that holds the attributes:
    - name: A string representing the person's name
    - age: An integer representing the person's age
    - is_student: A boolean indicating if the person is a student
    """

    def __init__(self, name, age, is_student):
        """
        Initialize the CustomObject with name, age, and is_student attributes.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the attributes of the object in a formatted string.
        """
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Serialize the current instance and save it to the specified file.
        Parameters:
            filename (str): The name of the file where the object will be saved
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except (pickle.PicklingError, OSError) as err:
            print("Failed to serialize object: {}".format(err))

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize the object from the specified file and return the instance.
        Parameters:
            filename (str): The name of the file from which to load the object.
        Returns:
            CustomObject: The deserialized instance of CustomObject,
            or None if failed.
        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
            return obj
        except (FileNotFoundError, pickle.UnpicklingError, OSError) as err:
            print("Failed to deserialize object: {}".format(err))
            return None
