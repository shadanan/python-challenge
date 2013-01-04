#!/usr/bin/env python
# encoding: utf-8

# Start with: readme.txt

# Yes! This is really level 21 in here. 
# And yes, After you solve it, you'll be in level 22!
# 
# Now for the level:
# 
# * We used to play this game when we were kids
# * When I had no idea what to do, I looked backwards.

# Let's start by reversing the data in package.pack

fp = open('package.pack', 'rb')
data = fp.read()
fp.close()
