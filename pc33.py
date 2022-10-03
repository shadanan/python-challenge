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

import pandas as pd

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)

pixels = pd.Series(list(src.getdata()))
pixels.value_counts().sort_index()
pixels.value_counts().sort_index().plot.bar(figsize=(12, 6))

import numpy as np

pd.DataFrame(np.array(src))
import sys

np.set_printoptions(threshold=sys.maxsize)

dst = src.copy()
for y in range(dst.height):
    for x in range(dst.width):
        if dst.getpixel((x, y)) % 2 == 0:
            dst.putpixel((x, y), 0)
        elif dst.getpixel((x, y)) % 2 == 1:
            dst.putpixel((x, y), 255)
dst

dst = Image.new(mode="RGB", size=(src.width // 3, src.height))
for y in range(dst.height):
    for x in range(dst.width):
        color = (
            src.getpixel((x * 3, y)),
            src.getpixel((x * 3 + 1, y)),
            src.getpixel((x * 3 + 2, y)),
        )
        dst.putpixel((x, y), color)
dst
