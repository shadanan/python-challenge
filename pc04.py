#!/usr/bin/env python
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/def/linkedlist.php

import urllib

def process_nothing(nothing):
    while True:
        fp = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s" % nothing)
        data = fp.read()
        if "nothing is" in data:
            nothing = data[data.find("nothing is"):].split()[2]
            print data
        else:
            break
    print data

process_nothing(12345)

# Page says "Yes. Divide by two and keep going."
# The last number was 16044 so...

process_nothing(16044/2)

# Result is peak.html
# Go to: http://www.pythonchallenge.com/pc/def/peak.html