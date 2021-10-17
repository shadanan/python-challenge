#!/usr/bin/env python3
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/return/balloons.html

# Can you tell the difference? It is the brightness...
# Go to: http://www.pythonchallenge.com/pc/return/brightness.html

# Source says: maybe consider deltas.gz

import difflib
import gzip
import io
import requests
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

response = requests.get('http://www.pythonchallenge.com/pc/return/deltas.gz',
                        auth=('huge', 'file'))
data = gzip.decompress(response.content).decode('utf-8')

# The file contains two sequences of lines... separate them.
left = [x.split('   ')[0] for x in data.splitlines()]
right = [x.split('   ')[1] for x in data.splitlines()]

# Looks like they are similar, but different. Separate into three streams,
# one for what's equal, one with the left and one with the right.
fp1 = io.BytesIO()
fp2 = io.BytesIO()
fp3 = io.BytesIO()

for x in difflib.ndiff(left, right, charjunk=None):
    # print(x)
    if x.startswith('  '):
        fp1.write(bytes([int(x, 16) for x in x[2:].split()]))
    elif x.startswith('- '):
        fp2.write(bytes([int(x, 16) for x in x[2:].split()]))
    elif x.startswith('+ '):
        fp3.write(bytes([int(x, 16) for x in x[2:].split()]))

Image.open(fp1).show()
Image.open(fp2).show()
Image.open(fp3).show()

# Go to: http://www.pythonchallenge.com/pc/hex/bin.html
# User: butter, Pass: fly
