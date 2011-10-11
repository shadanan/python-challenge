#!/usr/bin/env python
# encoding: utf-8

def save_to_file(file_name, data):
    fp = open(file_name, 'w')
    for c in data:
        fp.write(chr(c))
    fp.close()

fp = open('deltas', 'r')
data = fp.read()

lines = data.splitlines()
print "Total Lines: %d" % len(lines)
print "Elements per line: %d" % len(lines[0].split("   ")[0].split())

p1 = []
p2 = []
p3 = []
p4 = []

left_mode = 0
right_mode = 0

for line in lines:
    # print line
    
    if left_mode == 1:
        p3 += map(lambda x: int(x, 16), line[0:53].split())
    
    if right_mode == 1:
        p4 += map(lambda x: int(x, 16), line[56:].split())

    if left_mode == 0:
        temp = map(lambda x: int(x, 16), line[0:53].split())
        p1 += temp
        if len(temp) != 18:
            left_mode = 1
    
    if right_mode == 0:
        temp = map(lambda x: int(x, 16), line[56:].split())
        p2 += temp
        if len(temp) != 18:
            right_mode = 1
    
print len(p1)
print len(p2)
print len(p3)
print len(p4)

save_to_file('p1.png', p1)
save_to_file('p2.png', p2)
save_to_file('p3.png', p3)
save_to_file('p4.png', p4)

