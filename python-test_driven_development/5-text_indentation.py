#!/usr/bin/python3
"""

Module composed by a function that prints 2 new lines after ".?:" characters

"""


def text_indentation(text):
    """ Function that prints 2 new lines after ".?:" characters"""

    if type(text) is not str:
        raise TypeError("text must be a string")

    s = text[:]

    for ch in ".?:":
        list_text = s.split(ch)
        s = ""
        for i in list_text:
            i = i.strip(" ")
            s = i + ch if s is "" else s + "\n\n" + i + ch

    print(s[:-3], end="")
