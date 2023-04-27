#!/bin/bash
# sends a GET request to the URL, and displays the body of the response
if [[ `curl -sL -w '%{http_code}' $1 -o /dev/null` -eq "200"  ]]; then curl -sL "$1";fi
