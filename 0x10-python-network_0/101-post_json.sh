#!/bin/bash
# post request sender
curl -s -X POST -H 'Content-Type:application/json' "$1" -d @"$2"
