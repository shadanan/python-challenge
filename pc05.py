#!/usr/bin/env python
# encoding: utf-8

import urllib
import pickle

fp = urllib.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
data = pickle.loads(fp.read())

for line in data:
    lineout = []
    for token in line:
        lineout.append(token[0] * token[1])
    print "".join(lineout)