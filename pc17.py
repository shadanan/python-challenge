#!/usr/bin/env python3
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/return/romance.html

# Picture shows some cookies. And there's an image in the bottom left that is
# reminiscent of a previous challenge:
# Challenge 4: http://www.pythonchallenge.com/pc/def/linkedlist.php

# If we look at the php page headers, we see that it is in fact setting a
# cookie! The cookie value info indicates that we should follow busynothing.
# Let's assemble the cookies in the order of the busynothings starting with 12345

# The cookie data is URL encoded. So we need to decode and replace '+' with ' '.

import bz2
from urllib.parse import unquote_to_bytes
from xmlrpc.client import ServerProxy

import httpx

from utils import GZipDisabled

cookie_data = []
nothing = 12345

while True:
    url = f"http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing={nothing}"
    resp = httpx.get(url)

    next_char = resp.cookies["info"]
    data = resp.text
    cookie_data.append(next_char)

    print(f"Data: {data}  \tNext Char: {next_char}")

    if "busynothing is" in data:
        nothing = int(data[data.find("busynothing is") :].split()[2])
    else:
        break

bzip_data = unquote_to_bytes("".join([" " if x == "+" else x for x in cookie_data]))

# The cookie data looks like bz2 data... let's decompress
print(bz2.decompress(bzip_data).decode("utf-8"))

# The result is:
# is it the 26th already? call his father and inform him that 'the flowers are on their way'. he'll understand.
# That must mean mozart's father. According to Wikipedia, Leopold.
# Head back to the phone book from Challenge 13:

print("Calling Mozart's father, Leopold...")
server = ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php", GZipDisabled())
print(server.phone("Leopold"))

# Result is 555-VIOLIN.

# Go to: http://www.pythonchallenge.com/pc/stuff/violin.php
# and set the cookie value to 'the flowers are on their way'

resp = httpx.get(
    "http://www.pythonchallenge.com/pc/stuff/violin.php",
    cookies={"info": "the flowers are on their way"},
)
print(resp.text)

# Leopold says: "oh well, don't you dare to forget the balloons."
# Go to: http://www.pythonchallenge.com/pc/return/balloons.html
