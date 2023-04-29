#!/usr/bin/python3
"""Redoing task 1 but this time with request."""

import requests
import sys

if __name__ == '__main__':

    url = sys.argv[1]

    data = requests.get(url)
    content = data.content.decode("utf-8")
    print(data.headers["X-Request-Id"])
