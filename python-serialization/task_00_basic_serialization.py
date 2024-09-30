#!/usr/bin/env python3

import pickle


def serialize_and_save_to_file(data, filename):
    with open('data.pkl', 'wb') as file:
        pickle.dump(data, file)

def load_and_deserialize(filename):
    # Your code here to load and deserialize data from the specified file
    pass