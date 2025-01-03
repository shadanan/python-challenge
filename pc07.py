#!/usr/bin/env python3
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/def/oxygen.html

# It's an image with some gray values... maybe we should convert the
# grayscale colour to an ascii value? We're going to need the
# Python Imaging Library for this.

import io
import json

import httpx
from PIL import Image

from utils import get_pixel

response = httpx.get("http://www.pythonchallenge.com/pc/def/oxygen.png")
img = Image.open(io.BytesIO(response.content))

result = "".join(chr(get_pixel(img, (x, 50))[0]) for x in range(0, 608, 7))
print(result)

data = json.loads(result[result.find("[") :])
print("".join([chr(x) for x in data]))

# result is [105, 110, 116, 101, 103, 114, 105, 116, 121] -> convert back to ascii
# it says "integrity"
# Go to: http://www.pythonchallenge.com/pc/def/integrity.html
