#!/usr/bin/env python
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/return/balloons.html
# Can you tell the difference? It is the brightness...
# http://www.pythonchallenge.com/pc/return/brightness.html
# Source says: consider deltas.gz
# wget http://www.pythonchallenge.com/pc/return/deltas.gz
# gunzip deltas.gz

def to_binary(string):
    return 
    
left = []
right = []
li, ri = (0, 0)
bin_data = []

fp = open('deltas', 'r')
data = fp.read()
fp.close()

for line in data.splitlines():
    data = line[0:53].strip()
    if data != '':
        left.append(data)

    data = line[56:].strip()
    if data != '':
        right.append(data)

fp = open('deltas.png', 'w')

while li < len(left) or ri < len(right):
    if li == len(left):
        ri += 1
    
    elif ri == len(right):
        li += 1
    
    elif left[li] == right[ri]:
        fp.write("".join([chr(int(x, 16)) for x in left[li].split()]))
        li += 1
        ri += 1
    
    elif left[li] not in right[ri:ri + 2]:
        li += 1
    
    elif right[ri] not in left[li:li + 2]:
        ri += 1

fp.close()

# Open the file 'deltas.png' and you get '../hex/bin.html'