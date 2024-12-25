#!/usr/bin/env python3
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/ring/guido.html
# User: repeat, Pass: switch

# Photograph of various transparent things.
# Page title: "silence!"
# Image named: "whoisit.jpg"

# If you visit: http://www.pythonchallenge.com/pc/ring/glass.html
#   It says: "yes. this is a glass."

# If you visit: http://www.pythonchallenge.com/pc/ring/water.html
#   It says: "no, thank you."

# If you visit: http://www.pythonchallenge.com/pc/ring/transparent.html
#   It says: "yes! many transparent things in here."

# If you look at the source, there are many whitespace characters!

import bz2
import re

import httpx

response = httpx.get(
    "http://www.pythonchallenge.com/pc/ring/guido.html", auth=("repeat", "switch")
)

# Get the lines that are whitespace
whitespace_lines = [l for l in response.text.split("\n") if re.match(r"^\s*$", l)]

# Count the length of the whitespace lines
line_lengths = [len(l) for l in whitespace_lines]

# Convert the length data into bytes (looks like bzip!)
data = bytes(line_lengths)

# Bunzip - the result is: Isn't it clear? I am a yankeedoodle!
print(bz2.decompress(data).decode("utf-8"))

# Go to: http://www.pythonchallenge.com/pc/ring/yankeedoodle.html
# User: repeat, Pass: switch
