#!/usr/bin/env python
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/return/mozart.html

# Looks like we need to straighten this image a little. 
# Try alligning the pink pixels.

import Image

def straighten(source):
    target = source.copy()
    for y in range(source.size[1]):
        line = [source.getpixel((x, y)) for x in range(source.size[0])]
        pink = line.index(195)
        line = line[pink:] + line[:pink]
        for x, pixel in enumerate(line):
            target.putpixel((x, y), pixel)
    return target

out = straighten(Image.open("mozart.gif"))
out.save("mozart_out.gif")

# The resulting image shows "romance".

# Go to: http://www.pythonchallenge.com/pc/return/romance.html