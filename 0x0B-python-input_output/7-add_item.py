#!/usr/bin/python3

"""Add Item"""


def load_from_json_file(filename):
    """ Load from json file """

    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


def save_to_json_file(my_obj, filename):
    """
    hahahaahhah

    :param my_obj:ojbj
    :param filename:filename
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)


if __name__ == '__main__':
    from sys import argv
    import json

    li = []

    for i in argv[1:]:
        li.append(i)

    file_list: list = load_from_json_file("add_item.json")
    save_to_json_file((file_list + li), "add_item.json")
