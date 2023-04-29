#!/usr/bin/python3
"""Redoing task 2 but this time with requests."""

import requests
import sys

if __name__ == '__main__':

    url = sys.argv[1]
    email = sys.argv[2]
    data = requests.post(url, data={"email": email})
    content = data.content.decode("utf-8")
    print(content)
