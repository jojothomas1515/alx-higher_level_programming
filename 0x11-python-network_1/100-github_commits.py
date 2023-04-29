#!/usr/bin/python3
"""github commits."""

import requests
import sys

if __name__ == '__main__':

    owner_name = sys.argv[2]
    repo_name = sys.argv[1]
    url = "https://api.github.com/repos/{}/{}/commits"\
        .format(owner_name, repo_name)
    data = requests.get(url)
    for i in data.json():
        print("{}: {}".format(i.get('sha'), i['commit']['author']['name']))
