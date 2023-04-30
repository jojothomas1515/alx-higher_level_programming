#!/bin/bash
# catch me if you can
curl -s -X PUT 0.0.0.0:5000/catch_me -o /dev/null -w "%{redirect_url}"| xargs curl -sL -X PUT -H 'Origin:School' -F 'user_id= 98'
