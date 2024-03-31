#!/usr/bin/python3
"""
This script takes GitHub credentials (username and personal access token) and
uses the GitHub API to display the user's ID.
"""

import requests
import sys

if __name__ == "__main__":
    """
    Main entry point of the script.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"

    try:
        response = requests.get(url, auth=(username, password))
        data = response.json()
        print(data['id'])
    except:
        print("None")
