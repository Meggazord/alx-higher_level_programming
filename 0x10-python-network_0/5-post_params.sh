#!/bin/bash
# This script sends a POST request to the URL passed as an argument with the specified parameters, and displays the body of the response
curl -sS "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
