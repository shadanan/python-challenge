#!/usr/bin/env python
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/return/evil.html

# The file name of the image is evil1.jpg... try evil2.jpg?
# You get an image that says, "not jpg - _.gfx", okay. Let's get
# http://www.pythonchallenge.com/pc/return/evil2.gfx

# But... evil3.jpg exists. It says, "no more evils..."
# And evil4.jpg exists. It's a text file though, and it says
# "Bert is evil! go back!"

# Anyway, the binary soup looks like 5 image files shuffled
# together (hint is the deck of cards). Let's re-assemble.

import io
import requests
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

response = requests.get('http://www.pythonchallenge.com/pc/return/evil2.gfx',
                        auth=('huge', 'file'))
data = response.content

images = [Image.open(io.BytesIO(data[i::5])) for i in range(5)]

for image in images:
    image.show()

# This results in 5 images that spell out:
# (dis, pro, port, tional, ity), with the ity crossed out.

# Go to: http://www.pythonchallenge.com/pc/return/disproportional.html
