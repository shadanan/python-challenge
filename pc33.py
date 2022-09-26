#!/usr/bin/env python3
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/rock/beer.html
# User: kohsamui, Pass: thailand

# Picture of a barrel and several bottles of Jack Daniel's whiskey.
# Title: "33 bottles of beer on the wall"

# Comment in HTML:
#   If you are blinded by the light,
#   remove its power, with its might.
#   Then from the ashes, fair and square,
#   another truth at you will glare.

# The image src is beer1.jpg. If you navigate to beer2.jpg, you get an image that says:
# "no, png". Navigating to beer2.png reveals a black and white image with an X in the
# center that appears to be the start of the puzzle.

import io

import requests
from PIL import Image

# Grab the puzzle image.
response = requests.get(
    "http://www.pythonchallenge.com/pc/rock/beer2.png",
    auth=("kohsamui", "thailand"),
)
src = Image.open(io.BytesIO(response.content))
src.show()
