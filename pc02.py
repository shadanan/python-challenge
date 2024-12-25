#!/usr/bin/env python3
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/def/ocr.html
# Get the characters from the source of the page

from collections import Counter

import httpx

response = httpx.get("http://www.pythonchallenge.com/pc/def/ocr.html")
data = response.text.strip()
chars = data[data.find("%%") : -4]

hist = Counter(chars)

rarechars = [char for char, freq in hist.items() if freq == 1]
result = [char for char in chars if char in rarechars]
print("".join(result))

# Result is equality
# Go to: http://www.pythonchallenge.com/pc/def/equality.html
