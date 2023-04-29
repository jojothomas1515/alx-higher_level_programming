#!/bin/bash
# post request sender
curl -sX POST "$1" -d "$(echo "$(cat "$2")")"
