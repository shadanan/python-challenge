#!/usr/bin/env python3
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/ring/bell.html
# User: repeat, Pass: switch

# Photograph of a lagoon.
# Page title: "many pairs ring-ring"
# Caption:
#   RING-RING-RING
#   say it out loud

import io
from typing import cast

import httpx
from PIL import Image

response = httpx.get(
    "http://www.pythonchallenge.com/pc/ring/bell.png", auth=("repeat", "switch")
)
src = Image.open(io.BytesIO(response.content))

# There appears to be vertical lines encoded in the green channel.
src.show()


def getpixel(xy: tuple[int, int]) -> int:
    return cast(tuple[int, ...], src.getpixel(xy))[1]


# If you visit: http://www.pythonchallenge.com/pc/ring/green.html
#   It says: "yes! green!"

# The absolute difference between pixels is almost always 42:
nonpairs = []
dst = Image.new(mode="RGB", size=(src.width, src.height))
for y in range(src.height):
    for a, b in zip(range(0, src.width - 1, 2), range(1, src.width, 2)):
        if getpixel((a, y)) - getpixel((b, y)) == 42:
            dst.putpixel((a, y), (255, 0, 0))
            dst.putpixel((b, y), (255, 255, 255))
        elif getpixel((a, y)) - getpixel((b, y)) == -42:
            dst.putpixel((a, y), (255, 255, 0))
            dst.putpixel((b, y), (255, 255, 255))
        else:
            nonpairs.append(abs(getpixel((a, y)) - getpixel((b, y))))
dst.show()

# Decode the set of pairs that don't have a difference of 42.
# The result is: whodunnit().split()[0] ?
print(bytes(nonpairs).decode("utf-8"))

# So, who did Python? Guido!

# Go to: http://www.pythonchallenge.com/pc/ring/guido.html
# User: repeat, Pass: switch
