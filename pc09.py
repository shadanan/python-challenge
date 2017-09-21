#!/usr/bin/env python3
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/return/good.html
# un: huge, pw: file

# Source of the page says first+second=? and contains:
# The image reminds me of connect the dots. So, let's connect the dots...

import urllib.request
from PIL import Image, ImageDraw

password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(realm=None,
                          uri='http://www.pythonchallenge.com/pc/return/',
                          user='huge',
                          passwd='file')
auth_handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

opener = urllib.request.build_opener(auth_handler)
with opener.open('http://www.pythonchallenge.com/pc/return/good.html') as fp:
    lines = fp.read().decode('utf-8').strip().split('\n')

first = eval(f"[{''.join(lines[lines.index('first:')+1:lines.index('', lines.index('first:'))])}]")
second = eval(f"[{''.join(lines[lines.index('second:')+1:lines.index('', lines.index('second:'))])}]")

def connect_the_dots(draw, values):
    coords = list(zip(values[0::2], values[1::2]))
    for start, stop in zip(coords[0:-1], coords[1:]):
        draw.line(start + stop, fill=255)

image = Image.new('P', (500, 500))
draw = ImageDraw.Draw(image)
connect_the_dots(draw, first)
connect_the_dots(draw, second)
image.show()

# Looks like a picture of a bull...
# Go to: http://www.pythonchallenge.com/pc/return/bull.html
