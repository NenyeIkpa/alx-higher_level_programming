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
    request = urllib.request.Request(url, data=post_data)
    try:
        with urllib.request.urlopen(request) as response:
            body = response.read()
            to_str = body.decode('utf-8')
            print('your email is: {}'.format(to_str))
    except Exception as e:
        pass
