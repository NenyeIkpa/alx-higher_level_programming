#!/usr/bin/python3
"""
    takes in a URL and an email, sends a POST request to the passed URL
    with the email as a parameter, and displays the body of the response
    (decoded in utf-8)
"""
import urllib.request
import urllib.parse
from sys import argv


url = argv[1]
email = argv[2]
post_data = urllib.parse.urlencode({'email': email}).encode('utf-8')

try:
    with urllib.request.urlopen(url, data=post_data) as response:
        to_str = response.read().decode('utf-8')
        print('your email is: {}'.format(to_str))
except Exception as e:
    pass
