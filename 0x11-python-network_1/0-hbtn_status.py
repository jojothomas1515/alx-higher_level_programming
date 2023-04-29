#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status."""

import urllib.request as req

if __name__ == "__main__":
    with req.urlopen("https://alx-intranet.hbtn.io/status") as data:
        bd = data.read()
        msg = data.msg
        print("Body response:")
        print("\t- type: {}".format(type(bd)))
        print("\t- content: {}".format(bd))
        print("\t- utf8 content: {}".format(msg))
