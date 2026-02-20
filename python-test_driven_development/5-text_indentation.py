#!/usr/bin/python3
"""prints a text with 2 new lines after ., ? and :"""


def text_indentation(text):
    """prints formated text"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for i in range(len(text)):

        if text[i] == " " and i > 0 and text[i - 1] in ".?:":
            continue

        print(text[i], end="")

        if text[i] in ".?:":
            print()
            print()
