#!/usr/bin/python3
"""Redoing task one but this time with request."""

import requests

if __name__ == '__main__':

    url = "https://alx-intranet.hbtn.io/status"

    data = requests.get(url)
    content = data.content.decode("utf-8")
    print("Body response:\n\t- type: {}\n\t -content: {}"
          .format(type(content), content))
