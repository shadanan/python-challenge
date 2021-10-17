#!/usr/bin/env python3
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/hex/speedboat.html

# It's a photograph of a lake with mountains in the background.
# An oar is tracing a zigzag on the image.
# The title of the page is "between the tables".
# The photograph links to "../ring/bell.html" which asks for a username and password.
# The image is called zigzag.jpg but there's a comment that says "did you say gif?"
# There's a hint, "oh, and this is NOT a repeat of 14"

# In level 14, we changed the position of pixels to produce an image. The hint suggests
# that we should have to do something different.

import bz2
import io
import keyword

import requests
from PIL import Image

response = requests.get(
    "http://www.pythonchallenge.com/pc/hex/zigzag.gif", auth=("butter", "fly")
)

src = Image.open(io.BytesIO(response.content))
data = src.tobytes()

# The image data starts with d7 d0 cb 0c
print(data[:4].hex(" "))  # d7 d0 cb 0c

# The palette data seems to follow this pattern.
map = src.palette.palette[::3]
print(hex(map[0xD7]), hex(map[0xD0]), hex(map[0xCB]))  # 0xd0 0xcb 0x0c

# Collect the data where the pattern is broken.
img_data = [255 if map[a] != b else 0 for a, b in zip(data[0:-1], data[1:])]
dst = Image.new(mode="L", size=src.size)
dst.putdata(img_data)
dst.show()  # The image says, "not 🗝word", and below it "busy 2"

# Collect the second stream where the pattern is broken. It results in bz2 data.
bz2_data = [b for a, b in zip(data[0:-1], data[1:]) if map[a] != b]

# Decompressing the data results in mostly python keywords as text.
words = bz2.decompress(bytearray(bz2_data)).decode("utf-8").split()

# Remove all python keywords from the text as well as ../ring/bell.html.
# Need to add exec and print to the list because they are not python3 keywords.
keywords = keyword.kwlist + ["../ring/bell.html", "exec", "print"]
print({w for w in words if w not in keywords})  # {'repeat', 'switch'}

# Go to: http://www.pythonchallenge.com/pc/ring/bell.html
# User: repeat, Pass: switch
