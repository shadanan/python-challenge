#!/usr/bin/env python3
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/def/linkedlist.php

import urllib.request

def process_nothing(nothing):
    while True:
        url = f"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={nothing}"
        with urllib.request.urlopen(url) as fp:
            data = fp.read().decode('utf-8')
        if "nothing is" in data:
            nothing = data[data.find("nothing is"):].split()[2]
            print(data)
        else:
            break
    print(data)

process_nothing(12345)

# Page says "Yes. Divide by two and keep going."
# The last number was 16044 so...

process_nothing(16044/2)

# Result is peak.html
# Go to: http://www.pythonchallenge.com/pc/def/peak.html
