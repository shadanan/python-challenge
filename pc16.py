#!/usr/bin/env python3
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/return/mozart.html

# Looks like we need to straighten this image a little.
# Try alligning the pink pixels.

import io

import httpx
from PIL import Image

response = httpx.get(
    "http://www.pythonchallenge.com/pc/return/mozart.gif", auth=("huge", "file")
)
src = Image.open(io.BytesIO(response.content))


def straighten(source):
    target = source.copy()
    for y in range(source.size[1]):
        line = [source.getpixel((x, y)) for x in range(source.size[0])]
        pink = line.index(195)
        line = line[pink:] + line[:pink]
        for x, pixel in enumerate(line):
            target.putpixel((x, y), pixel)
    return target


out = straighten(src)
out.show()

# The resulting image shows "romance".
# Go to: http://www.pythonchallenge.com/pc/return/romance.html
