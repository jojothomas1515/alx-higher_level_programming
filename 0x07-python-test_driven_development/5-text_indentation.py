#!/usr/bin/python3

"""Text indentation module"""


def text_indentation(text):
    """Adds two newline when it encounter characters like '.?:'

    Args:
        text (str): text to preprocess and print

    """

    if not isinstance(text, str):
        raise (TypeError("text must be a string"))

    new_str = [i for i in text.split()]

    for i in new_str:
        if "." in i or ":" in i or "?" in i:
            new_str[new_str.index(i)] = i + "\n\n"

    for i in new_str:
        print("{}{}".format(i, " " if "\n" not in i else ""), end="")
