#!/usr/bin/env python

a = ['1', '11', '21', '1211', '111221']

while len(a) != 31:
    val = a[-1][0]
    count = 0
    next = []
    
    for x in a[-1]:
        if val == x:
            count += 1
        else:
            next.append(str(count))
            next.append(val)
            val = x
            count = 1
            
    next.append(str(count))
    next.append(val)
    a.append(''.join(next))

print len(a[30])