#!/usr/bin/env python
# encoding: utf-8

import urllib

def open(val):
    fp = urllib.urlopen("http://huge:file@www.pythonchallenge.com/pc/return/%s.html" % val)
    data = fp.read()
    return fp.code, data

