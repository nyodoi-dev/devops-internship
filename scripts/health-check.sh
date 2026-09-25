#!/bin/bash
url=$1
status=$(curl -s -o /dev/null -w "%{http_code}" "$url")
time=$(date)
echo "$time  | $url | $status" >>../logs/health-check.log

if [[ "$status" == 2* ]]; then 
    echo "Healthy"
    exit 0
else 
     echo "Unhealthy"
     exit 1
fi
