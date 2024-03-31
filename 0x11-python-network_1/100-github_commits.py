#!/usr/bin/python3
"""
This script retrieves the 10 most recent commits from a GitHub repository.
"""

import requests
import sys

if __name__ == "__main__":
    """
    Main entry point of the script.
    """
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    try:
        response = requests.get(url)
        data = response.json()
        for commit in data[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    except:
        print("An error occurred while fetching commits.")
