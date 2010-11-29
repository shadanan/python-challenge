#!/usr/bin/env python
# encoding: utf-8

import Image

src = Image.open('wire.png')
img = Image.new('RGB', (100, 100))
data = []

bnd = [0, 0, 99, 99]
vec = (1, 0)
pos = (0, 0)

for i in xrange(10000):
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
