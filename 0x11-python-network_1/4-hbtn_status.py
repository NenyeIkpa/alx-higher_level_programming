#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status."""
import requests


if __name__ == "__main__":
    outcome = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(outcome.text)))
    print("\t- content: {}".format(outcome.text))
