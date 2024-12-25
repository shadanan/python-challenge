#!/usr/bin/env python3
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/return/italy.html

# The image shows a spiral. And the HTML source contains the hint:
# <!-- remember: 100*100 = (100+99+99+98) + (...  -->
# Let's process the image "wire.png" in a spiral like fashion...

import io

import httpx
from PIL import Image

from utils import get_pixel

response = httpx.get(
    "http://www.pythonchallenge.com/pc/return/wire.png", auth=("huge", "file")
)
src = Image.open(io.BytesIO(response.content))

img = Image.new("RGB", (100, 100))
data = []

bnd = [0, 0, 99, 99]
vec = (1, 0)
pos = (0, 0)

for i in range(10000):
    img.putpixel(pos, get_pixel(src, (i, 0)))
    pos = pos[0] + vec[0], pos[1] + vec[1]

    if vec[0] == 1 and pos[0] == bnd[2]:
        vec = (0, 1)
        bnd[1] += 1
    elif vec[1] == 1 and pos[1] == bnd[3]:
        vec = (-1, 0)
        bnd[2] -= 1
    elif vec[0] == -1 and pos[0] == bnd[0]:
        vec = (0, -1)
        bnd[3] -= 1
    elif vec[1] == -1 and pos[1] == bnd[1]:
        vec = (1, 0)
        bnd[0] += 1

img.show()

# Result is a cat.
# Go to: http://www.pythonchallenge.com/pc/return/cat.html

# It says "and its name is uzi. you'll hear from him later."
# Go to: http://www.pythonchallenge.com/pc/return/uzi.html
