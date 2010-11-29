#!/usr/bin/env python
# encoding: utf-8

import os
import Image

fp = open("evil2.gfx", "rb")
data = fp.read()
fp.close()

files = []
for i in range(5):
    files.append(open('/tmp/pc12_image_%d.gif' % i, 'wb'))

for index, val in enumerate(data):
    files[index % 5].write(val)

for f in files:
    f.close()

for i in range(5):
    os.system('open /tmp/pc12_image_%d.gif' % i)
