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

# Grab the mandelbrot image.
response = requests.get(
    "http://www.pythonchallenge.com/pc/rock/mandelbrot.gif",
    auth=("kohsamui", "thailand"),
)
src = Image.open(io.BytesIO(response.content))

# Functions to generate a mandelbrot image.
def instability(c: complex, z: float = 0.0, n: int = 128, r: int = 2) -> int:
    for i in range(n):
        z = z**2 + c
        if abs(z) > r:
            return i
    return n - 1


def mandelbrot(l: float, t: float, w: float, h: float, vpw: int) -> Image.Image:
    vph = round(vpw / w * h)
    mandelbrot = Image.new(mode="L", size=(vpw, vph))
    for y in range(vph):
        for x in range(vpw):
            c = complex(l + x * w / vpw, t + y * h / vph)
            mandelbrot.putpixel((x, vph - y - 1), instability(c))
    return mandelbrot


# Generate a mandelbrot using the given window and number of iterations.
gen = mandelbrot(0.34, 0.57, 0.036, 0.027, 640)

# If we compare the gif with the generated image, we see that most pixels match.
# The ones that don't have a difference of either 16 or -16 which we encode as 0 and 1.
err = []
for y in range(src.height):
    for x in range(src.width):
        p = gen.getpixel((x, y)) - src.getpixel((x, y))
        if p == 16:
            err.append(0)
        elif p == -16:
            err.append(1)

# The resulting list contains 1679 values, whose factors are 23 and 73.
# Encode a bitmap image that is 23 x 73.
width, height = (23, 73)
img = Image.new(mode="L", size=(width, height))
for i, v in enumerate(err):
    img.putpixel((i % width, i // width), int(v * 255))
img.show()

# The resulting image is the Arecibo message:
# https://en.m.wikipedia.org/wiki/Arecibo_message

# Go to: http://www.pythonchallenge.com/pc/rock/arecibo.html
# User: kohsamui, Pass: thailand
