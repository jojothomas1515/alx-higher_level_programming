#!/usr/bin/python3
"""github authentication."""

import requests
import sys

if __name__ == '__main__':

    url = "https://api.github.com/authorizations"
    username = sys.argv[1]
    password = sys.argv[2]

    data = requests.get(url, auth=(username, password))
    res = data.content.decode()
    print(res)
