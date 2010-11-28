#!/usr/bin/env python
# encoding: utf-8
"""
pc12.py

Created by Shadanan Sharma on 2010-04-22.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import Image
import math

def factor(n):
    for i in xrange(1, int(math.sqrt(n))):
        if n % i == 0:
            print i, n/i

def partition(data, n):
    result = []
    for i in xrange(0, len(data), n):
        result.append(tuple(data[i:i+n]))
    return result

def shuffle(data):
    result = []
    for i in xrange(0, len(data), 5):
        result.append(data[i+4])
        result.append(data[i+3])
        result.append(data[i+1])
        result.append(data[i])
        result.append(data[i+2])
    return result

def flatten(data):
    result = []
    for i in data:
        result += i
    return result

def pick(data, k, n):
    result = []
    for i in xrange(len(data)):
        if i % n in k:
            result.append(data[i])
    return result

def main():
    fp = open("evil2.gfx", "rb")
    data = fp.read()
    fp.close()
    
    files = []
    for i in range(5):
        files.append(open('file%d.gif' % i, 'wb'))
    
    for index, val in enumerate(data):
        files[index % 5].write(val)
        # print index, str(val)
    # print "\n".join(map(str, data))
    
    for f in files:
        f.close()
    
    # data = partition(data, 5)
    # #data = e2data
    # oim = Image.new('RGB', (640, 480))
    # oim.putdata(data)
    # oim.show()

if __name__ == '__main__':
    main()

