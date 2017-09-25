#!/usr/bin/env python3
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/def/equality.html

import re
import requests

response = requests.get('http://www.pythonchallenge.com/pc/def/equality.html')
data = response.text
data = data[data.find('<!--')+5:-5]

# data = "abalsdkfABCsABCjalsdfAABzZZZsldkfj23"
print(''.join(re.findall(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', data)))

# Result is linkedlist
# Go to: http://www.pythonchallenge.com/pc/def/linkedlist.html
# Page displays: linkedlist.php
# Go to: http://www.pythonchallenge.com/pc/def/linkedlist.php
