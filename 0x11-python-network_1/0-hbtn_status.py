#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status."""

import urllib.request as req

with req.urlopen("https://alx-intranet.hbtn.io/status") as data:
    bd = data.read()
    msg = data.msg
    print(
        "Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
        .format(type(bd), bd, msg))
