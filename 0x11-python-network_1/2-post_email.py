#!/usr/bin/python3
"""
    takes in a URL and an email, sends a POST request to the passed URL
    with the email as a parameter, and displays the body of the response
    (decoded in utf-8)
"""
import urllib.request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    post_data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    try:
        with urllib.request.urlopen(url, data=post_data) as response:
            body = response.read()
            to_str = body.decode('utf-8')
            print(to_str)
    except Exception as e:
        pass
