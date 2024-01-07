#!/usr/bin/python3
"""
    fetches given url
"""
import urllib.request


try:
    with urllib.request.urlopen(
            'https://alx-intranet.hbtn.io/status'
            ) as response:
        body = response.read()
        bytes_to_string = body.decode('utf-8')
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:", bytes_to_string)
except Exception as e:
    pass
