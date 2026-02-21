#!/usr/bin/python3
"""prints a text with 2 new lines after ., ? and :"""



def text_indentation(text):
    """print formated text"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_line = True

    for i in range(len(text)):

        if new_line and text[i] == " ":
            continue

        print(text[i], end="")

        if text[i] in ".?:":
            if text[i + 1:].strip():
                print("")
                print("")
                new_line = True
            else:
                new_line = False
        else:
            new_line = False
