#!/bin/bash
# post request sender
curl -sX POST "$1" -d @"$2"
