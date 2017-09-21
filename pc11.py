#!/usr/bin/env python3

# Start at: http://www.pythonchallenge.com/pc/return/5808.html

# The title of the page is odd / even. Let's look at every other
# pixel and assemble it.

import urllib.request
from PIL import Image, ImageDraw

password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(realm=None,
                          uri='http://www.pythonchallenge.com/pc/return/',
                          user='huge',
                          passwd='file')
auth_handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

opener = urllib.request.build_opener(auth_handler)
with opener.open('http://www.pythonchallenge.com/pc/return/cave.jpg') as fp:
    src_image = Image.open(fp)

src_data = src_image.getdata()

dest_data = []
for index, value in enumerate(src_data):
    if (index // 640) % 2 == 0:
        if index % 2 == 0:
            dest_data.append(value)
    else:
        if index % 2 == 1:
            dest_data.append(value)

src_image.size

dest_image = Image.new('RGB', (640, 240))
dest_image.putdata(dest_data)
dest_image.show()

# Result is an image that says "evil".
# Go to: http://www.pythonchallenge.com/pc/return/evil.html
