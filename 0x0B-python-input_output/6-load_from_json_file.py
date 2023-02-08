#!/usr/bin/python3

""" Loading from a json file """
import json


def load_from_json_file(filename):
    """ Load from json file """

    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
