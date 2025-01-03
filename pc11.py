#!/usr/bin/env python3

# Start at: http://www.pythonchallenge.com/pc/return/5808.html

# The title of the page is odd / even. Let's look at every other
# pixel and assemble it.

import io

import httpx
from PIL import Image

response = httpx.get(
    "http://www.pythonchallenge.com/pc/return/cave.jpg", auth=("huge", "file")
)
src_image = Image.open(io.BytesIO(response.content))

src_data = src_image.getdata()

dest_data = []
for index, value in enumerate(src_data):
    if (index // 640) % 2 == 0:
        if index % 2 == 0:
            dest_data.append(value)

src_image.size

dest_image = Image.new("RGB", (320, 240))
dest_image.putdata(dest_data)
dest_image.show()

# Result is an image that says "evil".
# Go to: http://www.pythonchallenge.com/pc/return/evil.html
