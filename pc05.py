#!/usr/bin/env python3
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/def/peak.html
# The page says to pronounce it. It is a hill... peak hill... pickle (if you're French I guess?)
# And the source mentions banner.p... unpicke it!

import pickle

import httpx

response = httpx.get("http://www.pythonchallenge.com/pc/def/banner.p")
data = pickle.loads(response.content)

# The data basically specifies how to format some ascii characters

for line in data:
    lineout = []
    for char, freq in line:
        lineout.append(char * freq)
    print("".join(lineout))

# The result is an ascii picture that says "channel"
# Go to: http://www.pythonchallenge.com/pc/def/channel.html
