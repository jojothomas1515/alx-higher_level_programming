#!/bin/bash
# script takes in a URL, sends a request to that URL, and displays the size of the body of the response

curl -sI "$1" | grep -iP "content-length"| grep -oP "(\d+)"
