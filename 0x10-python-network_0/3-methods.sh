#!/bin/bash
# script takes in a URL and get all methods available
curl -sI -X OPTIONS "$1" | awk 'BEGIN {FS=":";} /^Allow/ {print $2;}'
