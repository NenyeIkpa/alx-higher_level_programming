#!/bin/bash
# sends a GET request to a URL, and displays the body of the response
curl -sfL "$1" -X GET
