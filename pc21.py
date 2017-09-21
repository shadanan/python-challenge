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

import bz2
import io
import logging
import requests
import zipfile
import zlib


# Load the zip file from the previous challenge
response = requests.get('http://www.pythonchallenge.com/pc/hex/unreal.jpg',
                        auth=('butter', 'fly'),
                        headers={'Range': f'bytes={1152983631}-'})
zf = zipfile.ZipFile(io.BytesIO(response.content))


# Open package.pack from the zip file using the password redavni
with zf.open('package.pack', pwd=b'redavni') as fp:
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

# The result is an ascii picture that says "copper"
# Visit http://www.pythonchallenge.com/pc/hex/copper.html
