#!/bin/bash
# post request sender
curl -sX POST "$1" -d "$(cat "$1")"
