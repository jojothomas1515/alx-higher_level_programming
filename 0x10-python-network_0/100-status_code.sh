#!/bin/bash
# Return the status code of the website
if [[ "$#" -lt "1" ]];then echo "No arguments passed";else curl -s -w '%{response_code}' "$1" -o /dev/null; fi
