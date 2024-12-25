#!/usr/bin/env python3
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/hex/copper.html

# Page title is "emulate", url is "copper", image is of an atari joystick. The
# source code says "or maybe white.gif would be more bright". Let's download
# white.gif!

import io

import httpx
from PIL import Image, ImageDraw

response = httpx.get(
    "http://www.pythonchallenge.com/pc/hex/white.gif", auth=("butter", "fly")
)
im = Image.open(io.BytesIO(response.content))

# white.gif contains 132 frames. Each frame has exactly one pixel that is not
# black at x, y in {98, 100, 102}.
pseq = []
for i in range(im.n_frames):  # type: ignore
    im.seek(i)
    for x in range(im.width):
        for y in range(im.height):
            if im.getpixel((x, y)) == (8, 8, 8):
                pseq.append((x, y))

# Let's interpret the one non-black pixel as a direction as if you were using
# a joystick (like the image!)
directions = [((x - 100), (y - 100)) for x, y in pseq]

# Split the directions up into segments, lifting the pen when directions is (0, 0)
segments = []
directions.insert(0, (0, 0))
for direction in directions:
    if direction == (0, 0):
        segment = []
        segments.append(segment)
        curr = (40 * len(segments), 25)
    curr = curr[0] + direction[0], curr[1] + direction[1]
    segment.append(curr)

# Now let's trace an image using the segments
image = Image.new("1", (250, 60))
draw = ImageDraw.Draw(image)
for segment in segments:
    draw.line(segment, fill="white")
image.show()

# The resulting image spells "bonus"!
# Next level: http://www.pythonchallenge.com/pc/hex/bonus.html
