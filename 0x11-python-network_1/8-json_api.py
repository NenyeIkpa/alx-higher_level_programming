#!/usr/bin/python3
"""
    takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter:
    The letter must be sent in the variable q, If no argument is given,
    set q="", If the response body is properly JSON formattedand not empty,
    display the id and name like this: [<id>] <name> else Display Not a
    valid JSON if the JSON is invalid, Display No result if the JSON is empty
"""
import sys
import requests


if __name__ == "__main__":
    letter = ""
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    payload = {"q": letter}
    response = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        outcome = response.json()
        if not outcome:
            print("No result")
        else:
            print("[{}] {}".format(outcome.get("id"), outcome.get("name")))
    except ValueError:
        print("Not a valid JSON")
