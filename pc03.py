#!/usr/bin/env python3
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/def/equality.html

import re
import urllib.request

with urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/equality.html") as fp:
    data = fp.read().decode('utf-8')
    data = data[data.find('<!--')+5:-5]

# data = "abalsdkfABCsABCjalsdfAABzZZZsldkfj23"
print("".join(re.findall(r"[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]", data)))

# Result is linkedlist
# Go to: http://www.pythonchallenge.com/pc/def/linkedlist.html
# Page displays: linkedlist.php
# Go to: http://www.pythonchallenge.com/pc/def/linkedlist.php
