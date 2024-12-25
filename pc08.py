#!/usr/bin/env python3
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/def/integrity.html

# It's a picture of a bee... the source contains an encoded un and pw.
# Use bz2 to decompress the username and password

import bz2

import httpx

response = httpx.get("http://www.pythonchallenge.com/pc/def/integrity.html")
data = response.content.decode()

fields = {}
for line in data[data.find("<!--") + 5 : data.find("-->")].strip().splitlines():
    key, value = line.split(": ")
    fields[key] = eval("b" + value)

print(bz2.decompress(fields["un"]).decode())
print(bz2.decompress(fields["pw"]).decode())

# Click on the bee and authorize using un: huge, pw: file
# You are redirected to: http://www.pythonchallenge.com/pc/return/good.html
