#!/usr/bin/env python3
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/def/linkedlist.php

import httpx


def process_nothing(nothing):
    while True:
        url = f"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={nothing}"
        data = httpx.get(url).text
        if "nothing is" in data:
            nothing = data[data.find("nothing is") :].split()[2]
            print(data)
        else:
            break
    print(data)


process_nothing(12345)

# Page says "Yes. Divide by two and keep going."
# The last number was 16044 so...

process_nothing(16044 / 2)

# Result is peak.html
# Go to: http://www.pythonchallenge.com/pc/def/peak.html
