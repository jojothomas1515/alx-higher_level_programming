#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST request to\
 the passed URL with the email as a parameter, and displays the body of the\
 response (decoded in utf-8)."""

from urllib.request import Request, urlopen
from urllib.error import HTTPError
import sys

if __name__ == '__main__':
    try:
        url = sys.argv[1]
        req = Request(url)
        with urlopen(req) as d:
            print(d.read().decode("utf-8"))
    except HTTPError as err:
        print("Error code: {}".format(err.getcode()))
