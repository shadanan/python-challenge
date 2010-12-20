#!/usr/bin/env python
# encoding: utf-8

import urllib

nothing = 12345
# nothing = 92118/2
while True:
    fp = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s" % nothing)
    data = fp.read()
    if "nothing is" in data:
        nothing = data[data.find("nothing is"):].split()[2]
        print data
    else:
        break
print data