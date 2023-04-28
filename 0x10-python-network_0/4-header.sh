#!/bin/bash
# setting headers with curl
curl -sI -X GET -H "X-School-User-Id: 98" "$1" 
