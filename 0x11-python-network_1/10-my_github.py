#!/usr/bin/python3
"""
"""
import requests
import sys


username = sys.argv[1]
access_token = sys.argv[2]
url = 'https://api.github.com/user'
auth_header = requests.auth.HTTPBasicAuth(username, access_token)

try:
    response = requests.get(url, auth=auth_header)

    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data.get('id')
        print(f"Your GitHub user ID is: {user_id}")
    else:
        print("None")

except requests.RequestException as e:
    print("None")
