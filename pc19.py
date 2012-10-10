#!/usr/bin/env python
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/hex/bin.html
# username: butter, password: fly

# You get a picture of india... 
# Try: http://www.pythonchallenge.com/pc/hex/india.html
# Hint: "nnn. what could this mean?"

# Try phoning from Challenge 13?
from xmlrpclib import ServerProxy
server = ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")

print server.phone("please!")
