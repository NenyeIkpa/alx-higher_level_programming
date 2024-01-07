#!/bin/bash
# sends a request to a given url and displays the size of the body of the response
curl $1 -X GET --write-out ${size_download} -s
