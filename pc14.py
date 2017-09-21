#!/usr/bin/env python3
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/return/italy.html

# The image shows a spiral. And the HTML source contains the hint:
# <!-- remember: 100*100 = (100+99+99+98) + (...  -->
# Let's process the image "wire.png" in a spiral like fashion...

import urllib.request
from PIL import Image

password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(realm=None,
                          uri='http://www.pythonchallenge.com/pc/return/',
                          user='huge',
                          passwd='file')
auth_handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

opener = urllib.request.build_opener(auth_handler)
with opener.open('http://www.pythonchallenge.com/pc/return/wire.png') as fp:
    src = Image.open(fp)

img = Image.new('RGB', (100, 100))
data = []

bnd = [0, 0, 99, 99]
vec = (1, 0)
pos = (0, 0)

for i in range(10000):
    img.putpixel(pos, src.getpixel((i, 0)))
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
