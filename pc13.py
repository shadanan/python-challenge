#!/usr/bin/env python
# encoding: utf-8

from xmlrpclib import ServerProxy
server = ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")

print server.phone("Bert")
