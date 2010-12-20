#!/usr/bin/env python
# encoding: utf-8

import urllib2
import bz2
from xmlrpclib import ServerProxy

cookie_data = []
nothing = 12345
bhandle = bz2.BZ2Decompressor()

while True:
    response = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=%s" % nothing)
    
    cookies = [x[1].split(";")[0] for x in response.info().items() if x[0] == 'set-cookie']
    data = response.read()
    
    next_char = cookies[0][5:]
    if next_char == "+":
        next_char = " "
    elif next_char.startswith("%"):
        next_char = chr(int(next_char[1:], 16))
    
    cookie_data.append(next_char)
    print "Data: %s  \tCookies: %s  \tNext Char: %s" % (data, ", ".join(cookies), hex(ord(next_char)))
    
    if "busynothing is" in data:
        nothing = int(data[data.find("busynothing is"):].split()[2])
    else:
        break

print len(cookie_data)
print bz2.decompress("".join(cookie_data))

print "Calling Mozart's father, Leopold..."
server = ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print server.phone("Leopold")
