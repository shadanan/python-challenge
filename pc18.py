#!/usr/bin/env python
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/return/balloons.html

# Can you tell the difference? It is the brightness...
# Go to: http://www.pythonchallenge.com/pc/return/brightness.html

# Source says: consider deltas.gz
# wget http://www.pythonchallenge.com/pc/return/deltas.gz
# gunzip deltas.gz

import difflib

def to_binary(string):
    return 
    
left = []
right = []
li, ri = (0, 0)
bin_data = []

fp = open('deltas', 'r')
data = fp.read()
fp.close()

# The file contains two sequences of lines... separate them.

for line in data.splitlines():
    data = line[0:53].strip()
    if data != '':
        left.append(data)

    data = line[56:].strip()
    if data != '':
        right.append(data)

# Looks like they are similar, but different. Separate into three streams,
# one for what's equal, one with the left and one with the right.

fp1 = open('deltas_equal.png', 'wb')
fp2 = open('deltas_minus.png', 'wb')
fp3 = open('deltas_plus.png', 'wb')

for x in difflib.ndiff(left, right):
    # print x
    if x.startswith('  '):
        fp1.write("".join([chr(int(c, 16)) for c in x[2:].split()]))
    elif x.startswith('-'):
        fp2.write("".join([chr(int(c, 16)) for c in x[2:].split()]))
    elif x.startswith('+'):
        fp3.write("".join([chr(int(c, 16)) for c in x[2:].split()]))

fp1.close()
fp2.close()
fp3.close()

# Open the file 'deltas_equal.png' and you get '../hex/bin.html'
# Open the file 'deltas_minus.png' and you get 'fly' (password)
# Open the file 'deltas_plus.png' and you get 'butter' (username)
# Looks like I got it backwards...

# Go to: http://www.pythonchallenge.com/pc/hex/bin.html