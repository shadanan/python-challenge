#!/usr/bin/env python3
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/ring/grandpa.html
# User: repeat, Pass: switch

# Photograph of the grandfather and grandmother rocks in Koh Samui, Thailand.
# Page title: Where am I
# Image named: grandpa.jpg
# HTML comment: <!-- short break, this ***REALLY*** has nothing to do with Python -->
# Image is linked to password protected page.

# Taking the comment at its word, try:
# User: kohsamui, Pass: thailand

# URL: http://www.pythonchallenge.com/pc/rock/grandpa.html
# User: kohsamui, Pass: thailand

# Picture of the mandelbrot set.
# Page title: UFOs ?
# Image named: mandelbrot.gif
# Caption: That was too easy. You are still on 31...
# There are two non-standard HTML tags in the img tag:
#   <window left="0.34" top="0.57" width="0.036" height="0.027"/>
#   <option iterations="128"/>

import io

import requests
from PIL import Image

response = requests.get(
    "http://www.pythonchallenge.com/pc/rock/mandelbrot.gif",
    auth=("kohsamui", "thailand"),
)
src = Image.open(io.BytesIO(response.content))
src.show()
