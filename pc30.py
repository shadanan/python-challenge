#!/usr/bin/env python3
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/ring/yankeedoodle.html
# User: repeat, Pass: switch

# Photograph of a beach with lounge chairs and umbrellas
# Page title: "relax you are on 30"
# Image named: "yankeedoodle.jpg"
# Caption: "The picture is only meant to help you relax"
# Comment in HTML: "<!-- while you look at the csv file -->"

import math

import httpx
import pandas as pd
from PIL import Image

# Grab the CSV file.
response = httpx.get(
    "http://www.pythonchallenge.com/pc/ring/yankeedoodle.csv", auth=("repeat", "switch")
)

# Read the data into a pandas Series.
str_data = [v.strip() for v in response.text.split(",")]
values = pd.Series([float(v) for v in str_data])

# There are 7637 values whose factors are 53 and 139.
# Let's interpret the data as grayscale image data.
width = 139
height = math.ceil(len(values) / width)
img = Image.new(mode="L", size=(width, height))
for i, v in enumerate(values):
    img.putpixel((i // height, i % height), int(v * 255))
img.show()

# The result is an image with the following text:

# n=str(x[i])[5]
#  +str(x[i+1])[5]
#  +str(x[i+2])[6]

# Let's extract bytes according to this from the values:
data = []
for i in range(0, len(str_data) - 2, 3):
    n = int(str_data[i][5] + str_data[i + 1][5] + str_data[i + 2][6])
    data.append(n)
print(bytes(data).decode("utf-8"))

# The result contains a long bit of text starting with:
# So, you found the hidden message.
# There is lots of room here for a long message, but we only need very little space to
# say "look at grandpa", so the rest is just garbage.

# Go to: http://www.pythonchallenge.com/pc/ring/grandpa.html
# User: repeat, Pass: switch
