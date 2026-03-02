#!/usr/bin/python3
"""This module defines a function to instance to a JSON-serializable dictionary."""

def class_to_json(obj):
    """Convert a class instance to a JSON-serializable dictionary."""
    return obj.__dict__
