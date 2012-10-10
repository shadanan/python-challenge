#!/usr/bin/env python
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/def/integrity.html

# It's a picture of a bee... the source contains an encoded un and pw.
# Use bz2 to decompress the username and password

import bz2
print bz2.decompress('BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')
print bz2.decompress('BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')

# un: huge, pw: file
# You are redirected to: http://www.pythonchallenge.com/pc/return/good.html