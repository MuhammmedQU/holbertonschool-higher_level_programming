#!/usr/bin/python3
"""prints a text with 2 new lines after ., ? and :"""


def text_indentation(text):
    """prints formated text"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for i in text:
        print(i, end="")
        if i in ".?:":
            print("\n\n", end="")
