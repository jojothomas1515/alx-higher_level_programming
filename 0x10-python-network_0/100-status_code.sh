#!/bin/bash
# Return the status code of the website
curl -s -w '%{response_code}' "$1" -o /dev/null
