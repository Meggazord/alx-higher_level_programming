#!/bin/bash
# This script sends a GET request to the URL passed as an argument with a custom header X-School-User-Id set to 98, and displays the body of the response
curl -sS "$1" -X GET -H "X-School-User-Id: 98"
