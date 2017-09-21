#!/usr/bin/env python3
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/hex/copper.html

# Page title is "emulate", url is "copper", image is of an atari joystick. The
# source code says "or maybe white.gif would be more bright". Let's download
# white.gif!

import urllib.request
from PIL import Image, ImageDraw

password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(realm=None,
                          uri='http://www.pythonchallenge.com/pc/hex/',
                          user='butter',
                          passwd='fly')
auth_handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

opener = urllib.request.build_opener(auth_handler)
with opener.open('http://www.pythonchallenge.com/pc/hex/white.gif') as src:
    im = Image.open(src)

# white.gif contains 132 frames. Each frame has exactly one pixel that is not
# black at x, y in {98, 100, 102}.
pseq = []
for i in range(im.n_frames):
    im.seek(i)
    for x in range(im.width):
        for y in range(im.height):
            if im.getpixel((x, y)) != 0:
                pseq.append((x, y))

# Let's interpret the one non-black pixel as a direction as if you were using
# a joystick (like the image!)
directions = [((x - 100), (y - 100)) for x, y in pseq]

# Now let's trace an image using the directions
image = Image.new('P', (250, 60))
draw = ImageDraw.Draw(image)
offset = 0
curr = (offset, 25)

for direction in directions:
    if direction == (0, 0):
        offset += 40
        curr = (offset, 25)
    stop = curr[0] + direction[0], curr[1] + direction[1]
    draw.line(curr + stop, fill=255)
    curr = stop

image.show()

# The resulting image spells "bonus"!
# Next level: http://www.pythonchallenge.com/pc/hex/bonus.html
