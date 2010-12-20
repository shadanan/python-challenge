#!/usr/bin/env python
# encoding: utf-8

import Image
src = Image.open('mozart.gif')
dest = Image.new('P', (1500, 500))
dest.putpalette(src.getpalette())

counter = 0
posx, posy = 0, 0

for index, pixel in enumerate(src.getdata()):
    dest.putpixel((posx, posy), pixel)
    
    if counter == 5:
        posy += 1
        posx = 0
    
    if pixel == 195:
        counter += 1
    else:
        counter = 0
    
    posx += 1

dest.show()