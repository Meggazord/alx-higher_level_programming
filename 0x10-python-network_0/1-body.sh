#!/bin/bash
# This script takes a URL as an argument, sends a GET request to the URL, and displays the body of the response
curl -sS "$1" -X GET -w "\n%{http_code}" | awk 'END {if ($NF == 200) {print $0}}'
