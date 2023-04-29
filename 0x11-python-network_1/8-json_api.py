#!/usr/bin/python3
"""Json api task."""

import requests
import sys

if __name__ == '__main__':

    url = "http://0.0.0.0:5000/search_user"
    try:
        q = sys.argv[1]
    except IndexError:
        q = ""
    data = requests.post(url, data={'q': q})
    res = data.json()
    if len(res) == 0:
        print("No result")
    else:
        try:
            print("[{}] {}"
                  .format(res['id'],
                          res['name']))
        except Exception:
            print("Not a valid JSON")
