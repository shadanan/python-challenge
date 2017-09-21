#!/usr/bin/env python3
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/def/peak.html
# The page says to pronounce it. It is a hill... peak hill... pickle (if you're French I guess?)
# And the source mentions banner.p... unpicke it!

import pickle
import urllib.request

with urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p") as fp:
    data = pickle.loads(fp.read())

# The data basically specifies how to format some ascii characters

for line in data:
    lineout = []
    for token in line:
        lineout.append(token[0] * token[1])
    print("".join(lineout))

# The result is an ascii picture that says "channel"
# Go to: http://www.pythonchallenge.com/pc/def/channel.html
