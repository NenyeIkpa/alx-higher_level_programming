#!/usr/bin/python3
"""
    takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id
"""
import requests
import sys


username = sys.argv[1]
access_token = sys.argv[2]
url = 'https://api.github.com/user'

if __name__ == "__main__":
    auth_header = requests.auth.HTTPBasicAuth(username, access_token)
    response = requests.get(url, auth=auth_header)
    github_id = response.json().get("id")
    print(github_id)
