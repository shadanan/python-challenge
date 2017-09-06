#!/usr/bin/env python3
# encoding: utf-8

# Start with: readme.txt

# Yes! This is really level 21 in here.
# And yes, After you solve it, you'll be in level 22!
#
# Now for the level:
#
# * We used to play this game when we were kids
# * When I had no idea what to do, I looked backwards.

# Looks like package.pack is zlib compressed data:
#
#     $ file package.pack
#     package.pack: zlib compressed data
#
# After exploration by decompressing, writing to a file and checking file type
# repeatedly, it looks like package.pack is compressed multiple times with:
#
#    * bzip2
#    * zlib
#
# Sometimes the data is reversed!
# We'll look at the header, apply the correct decompression in a loop.
#
# After decompressing and printing the final string decompressed, it says:
# "look at your logs". They want us to trace the sequence of operations. So
# every time we zlib decompress, write a space. Every time we bz2 decompressed
# write an x. Every time we reverse, write a new line.

import zlib
import bz2
import logging
logging.basicConfig(level=logging.DEBUG)

with open('package.pack', 'rb') as fp:
    sequence = []
    data = fp.read()
    while True:
        if data.startswith(b'x\x9c'):
            data = zlib.decompress(data)
            sequence.append(' ')
        elif data.startswith(b'BZ'):
            data = bz2.decompress(data)
            sequence.append('x')
        elif data.endswith(b'\x9cx') or data.endswith(b'ZB'):
            data = bytes(reversed(data))
            sequence.append('\n')
        else:
            print(bytes(reversed(data)).decode('utf-8'))
            break

len(sequence)
print(''.join(sequence))

# The result is:
#      xxx          xxx      xxxxxxxx    xxxxxxxx    xxxxxxxxxx  xxxxxxxx
#    xxxxxxx      xxxxxxx    xxxxxxxxx   xxxxxxxxx   xxxxxxxxx   xxxxxxxxx
#   xx     xx    xx     xx   xx      xx  xx      xx  xx          xx      xx
#  xx           xx       xx  xx      xx  xx      xx  xx          xx      xx
#  xx           xx       xx  xxxxxxxxx   xxxxxxxxx   xxxxxxxx    xxxxxxxxx
#  xx           xx       xx  xxxxxxxx    xxxxxxxx    xxxxxxxx    xxxxxxxx
#  xx           xx       xx  xx          xx          xx          xx   xx
#   xx     xx    xx     xx   xx          xx          xx          xx    xx
#    xxxxxxx      xxxxxxx    xx          xx          xxxxxxxxx   xx     xx
#      xxx          xxx      xx          xx          xxxxxxxxxx  xx      xx

# Visit http://www.pythonchallenge.com/pc/hex/copper.html
