#!/usr/bin/python3
"""work code with Json."""

import json


def serialize_and_save_to_file(data, filename):
    """Serialize data to JSON and save to a file."""
    with open(filename, "w") as file:
        json.dump(data, file)
           
def load_and_deserialize(filename):
    """Load JSON data from a file and deserialize it."""
    with open(filename, "r") as file:
        data = json.load(file)
    return data
