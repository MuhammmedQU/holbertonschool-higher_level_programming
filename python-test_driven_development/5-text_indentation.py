#!/usr/bin/python3
"""prints a text with 2 new lines after ., ? and :"""


def text_indentation(text):
    """print formatted text"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_line = True

    for i in range(len(text)):

        if new_line and text[i] == " ":
            continue

        if text[i] in ".?:":
            print(text[i])
            if i != len(text) - 1:
                print()
            new_line = True
        else:
            print(text[i], end="")
            new_line = False
