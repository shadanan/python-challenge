#!/usr/bin/env python3
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/return/mozart.html

# Looks like we need to straighten this image a little.
# Try alligning the pink pixels.

import io
import urllib.request
from PIL import Image

password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(realm=None,
                          uri='http://www.pythonchallenge.com/pc/return/',
                          user='huge',
                          passwd='file')
auth_handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

opener = urllib.request.build_opener(auth_handler)
with opener.open('http://www.pythonchallenge.com/pc/return/mozart.gif') as fp:
    src = Image.open(fp)

def straighten(source):
    target = source.copy()
    for y in range(source.size[1]):
        line = [source.getpixel((x, y)) for x in range(source.size[0])]
        pink = line.index(195)
        line = line[pink:] + line[:pink]
        for x, pixel in enumerate(line):
            target.putpixel((x, y), pixel)
    return target

out = straighten(src)
out.show()

# The resulting image shows "romance".
# Go to: http://www.pythonchallenge.com/pc/return/romance.html
