#!/usr/bin/python3
"""Redoing task 3 but this time with requests."""

import requests
import sys

if __name__ == '__main__':

    url = sys.argv[1]
    data = requests.get(url)
    if data.status_code >= 400:
        print("Error code: {}".format(data.status_code))
    else:
        print(data.content.decode("utf-8"))
