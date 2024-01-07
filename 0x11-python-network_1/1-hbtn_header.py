#!/usr/bin/python3
"""
     sends a request to the given URL and displays the value of the
     X-Request-Id variable found in the header of the response
"""
import urllib.request
from sys import argv


try:
    with urllib.request.urlopen(argv[1]) as response:
        x_request_id = response.headers.get('X-Request-Id')
        print(x_request_id)
except Exception as e:
    pass
