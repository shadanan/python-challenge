#!/usr/bin/env python

# Start at: http://www.pythonchallenge.com/pc/return/5808.html

# The title of the page is odd / even. Let's look at every other
# pixel and assemble it.

import Image

src_image = Image.open('cave.jpg')
src_data = src_image.getdata()

dest_data = []
for index, value in enumerate(src_data):
    if (index / 640) % 2 == 0:
        if index % 2 == 0:
            dest_data.append(value)
    else:
        if index % 2 == 1:
            dest_data.append(value)

dest_image = Image.new('RGB', (640, 320))
dest_image.putdata(dest_data)
dest_image.show()

# Result is an image that says "evil".
# Go to: http://www.pythonchallenge.com/pc/return/evil.html