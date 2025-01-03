#!/usr/bin/env python3
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/return/disproportional.html

# From the previous level, we know that Bert is evil. A button on the image
# of the phone takes us to '../phonebook.php'. The result is some sort of
# XML file. This must be an RPC call...

from xmlrpc.client import ServerProxy

from utils import GZipDisabled

server = ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php", GZipDisabled())

print(server.phone("Bert"))

# The phonebook has the number 555-ITALY for Bert
# Go to: http://www.pythonchallenge.com/pc/return/italy.html
