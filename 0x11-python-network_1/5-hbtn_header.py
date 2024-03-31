#!/usr/bin/python3
"""
5-hbtn_header.py - Python script to fetch the value of the X-Request-Id header from a URL's response.
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    request_id = response.headers.get('X-Request-Id')
    print(request_id)
