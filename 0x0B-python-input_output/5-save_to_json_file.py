#!/usr/bin/python3

"""save json file"""
import json


def save_to_json_file(my_obj, filename):
    """
    hahahaahhah

    :param my_obj:ojbj
    :param filename:filename
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
