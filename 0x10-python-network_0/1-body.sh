#!/usr/bin/bash
# sends a GET request to a URL, and displays the body of the response
curl -s -w "${response_code}" "$1"
