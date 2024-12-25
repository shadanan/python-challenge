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
from math import sqrt

import httpx
from IPython.display import display
from PIL import Image

# Grab the puzzle image.
response = httpx.get(
    "http://www.pythonchallenge.com/pc/rock/beer2.png",
    auth=("kohsamui", "thailand"),
)
src = Image.open(io.BytesIO(response.content))
src.show()

# Iterate over the image data selecting only those pixels that are less than or equal
# to a specific max brightness. If the remaining data forms a perfect square, render
# the pixels that are equal to the max brightness as white, and black otherwise.

images = {}
for pixel in reversed(sorted(set(src.getdata()))):
    data = [1 if p == pixel else 0 for p in src.getdata() if p <= pixel]
    root = int(sqrt(len(data)))
    if root * root != len(data):
        continue
    dst = Image.new("1", (root, root))
    dst.putdata(data)
    images[pixel] = dst

# This results in a number of letters, some of which are surrounded by a box. These
# letters spell out the word "gremlins".
for pixel in [98, 86, 62, 56, 44, 32, 26, 14]:
    images[pixel].show()

# Go to: http://www.pythonchallenge.com/pc/rock/gremlins.html
# User: kohsamui, Pass: thailand

# We've reached the Temporary End!
