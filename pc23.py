#!/usr/bin/env python3
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/hex/bonus.html

# There a picture of a cow

# Page title is "what is this module?"

# Comment after bonus.jpg:
# it can't find it. this is an undocumented module.

# And one last footer comment:
# 'va gur snpr bs jung?'

# this is *literally* an undocumented module
import re
import this

# We can decode 'va gur snpr bs jung?' using the encoding provided in this.d:
print(''.join([this.d.get(c, c) for c in 'va gur snpr bs jung?']))
# Result is: 'in the face of what?'

# When you import this, it prints out the zen of python.
zen = ''.join(this.d.get(c, c) for c in this.s)

# The line starting with 'In the face of' is: ambiguity
print(re.findall(r'In the face of ([a-z]+)', zen)[0])

# Next level: http://www.pythonchallenge.com/pc/hex/ambiguity.html
