#!/usr/bin/python3

"""Add Item"""

if __name__ == '__main__':
    from sys import argv
    import json

    save_to_json_file = __import__(
            '5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__(
            '6-load_from_json_file').load_from_json_file
    li = []

    for i in argv[1:]:
        li.append(i)

    file_list: list = load_from_json_file("add_item.json")
    save_to_json_file((file_list + li), "add_item.json")
