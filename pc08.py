#!/usr/bin/env python3
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/def/integrity.html

# It's a picture of a bee... the source contains an encoded un and pw.
# Use bz2 to decompress the username and password

import bz2
import requests

response = requests.get('http://www.pythonchallenge.com/pc/def/integrity.html')
data = response.content

def extract_field(data, field):
    field_index = data.find(field)
    first_quote_index = data.find(b"'", field_index) + 1
    last_quote_index = data.find(b"'", first_quote_index)
    return eval(b"b'%s'" % data[first_quote_index:last_quote_index])

un = extract_field(data, b'un')
pw = extract_field(data, b'pw')

print(bz2.decompress(un))
print(bz2.decompress(pw))

# Click on the bee and authorize using un: huge, pw: file
# You are redirected to: http://www.pythonchallenge.com/pc/return/good.html
