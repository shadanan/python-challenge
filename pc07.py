#!/usr/bin/env python
# encoding: utf-8

import Image

img = Image.open(open('oxygen.png', 'r'))

result = []
for x in xrange(0, 608, 7):
    result.append(chr(img.getpixel((x, 50))[0]))
result = "".join(result)

print result
print "".join(map(chr, eval(result[result.find('['):])))