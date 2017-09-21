#!/usr/bin/env python3
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/def/ocr.html
# Get the characters from the source of the page

import urllib.request

with urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html") as fp:
    data = fp.read().decode('utf-8').strip()
    chars = data[data.find('%%'):-4]

hist = {}
for char in chars:
    hist[char] = hist.get(char, 0) + 1

rarechars = [x[0] for x in hist.items() if x[1] == 1]
result = []
for char in chars:
    if char in rarechars:
        result.append(char)
print("".join(result))

# Result is equality
# Go to: http://www.pythonchallenge.com/pc/def/equality.html
