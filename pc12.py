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

import os
import Image

fp = open("evil2.gfx", "rb")
data = fp.read()
fp.close()

files = []
for i in range(5):
    files.append(open('evil%d.gif' % i, 'wb'))

for index, val in enumerate(data):
    files[index % 5].write(val)

for f in files:
    f.close()

# This results in 5 files that spell out:
# (dis, pro, port, tional, ity), with the ity crossed out.
# The "tional" is only have visible. 

# Go to: http://www.pythonchallenge.com/pc/return/disproportional.html