#!/bin/bash
# sends a GET request to the URL, and displays the body of the response
if [[ `curl -s -w '%{http_code}' $1 -o /dev/null` -eq "200"  ]]; then curl -s "$1";fi
