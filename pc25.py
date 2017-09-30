#!/usr/bin/env python3
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/hex/lake.html

# It's a picture of a calm lake with a puzzle piece overlay
# Title of the page is "imagine how they sound"
# There's a comment next to the image: "can you see the waves?"

# Well, it looks like there are files at lake{N}.wav

import io
import itertools
import requests
import tempfile
import wave
from PIL import Image


datas = []
for i in itertools.count(1):
    response = requests.get(f'http://www.pythonchallenge.com/pc/hex/lake{i}.wav',
                            auth=('butter', 'fly'))
    if response.status_code == 200:
        datas.append(response.content)
    else:
        break

waves = [wave.open(io.BytesIO(r)) for r in datas]
frames = [w.readframes(w.getnframes()) for w in waves]

# The hint "can you see the waves?" prompted me to put the data into an image.
# The puzzle piece overlay hints at the layout of the image data.

img = Image.new('RGB', (300, 300))
for i, frame in enumerate(frames):
    x_offset, y_offset = (i % 5) * 60, (i // 5) * 60
    for j, color in enumerate(zip(frame[0::3], frame[1::3], frame[2::3])):
        img.putpixel((j % 60 + x_offset, j // 60 + y_offset), color)

# The image is the original image with the word "decent" written on it
img.show()

# Go to: http://www.pythonchallenge.com/pc/hex/decent.html
