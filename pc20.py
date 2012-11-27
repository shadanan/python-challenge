#!/usr/bin/env python
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/hex/idiot2.html
# username: butter, password: fly

# If you look at the response headers for unreal.jpg, we notice that there's
# a suspicious: "Content-Range: bytes 0-30202/2123456789"

# If you try to ask for data beyond 30202, you get:
# "Why don't you respect my privacy?"
# Maybe we should read even further ahead? Perhaps loop over the end value?

import os
import httplib
import base64

def read_unreal(start, stop = ''):
    conn = httplib.HTTPConnection('www.pythonchallenge.com')
    conn.putrequest('GET', '/pc/hex/unreal.jpg')
    
    range_string = 'bytes=%s-%s' % (start, stop)
    conn.putheader('Range', range_string)
    
    auth_string = base64.encodestring('butter:fly').replace('\n', '')
    conn.putheader('Authorization', 'Basic %s' % auth_string)
    
    conn.endheaders()
    conn.send('')
    response = conn.getresponse()
    
    nrange = response.getheader('Content-Range')
    if nrange is None:
        return None
    result = [int(x) for x in nrange.split(' ')[1].split('/')[0].split('-')]
    result.append(response.read())
    
    conn.close()
    return result

pos = 30203
while True:
    curr = read_unreal(pos)
    if curr is None:
        break
    print curr
    pos = curr[1] + 1

# The result is:
# [30203, 30236, "Why don't you respect my privacy?\n"]
# [30237, 30283, 'we can go on in this way for really long time.\n']
# [30284, 30294, 'stop this!\n']
# [30295, 30312, 'invader! invader!\n']
# [30313, 30346, 'ok, invader. you are inside now. \n']

# If we visit: http://www.pythonchallenge.com/pc/hex/invader.html
# We get: "Yes! that's you!"

# Let's try reading from 2123456789

print read_unreal(2123456789)

# It result is:
# [2123456744, 2123456788, 'esrever ni emankcin wen ruoy si drowssap eht\n']
# That is, 'the password is your new nickname in reverse'. It must mean
# 'invader' backwards ('redavni')
# Let's try going down a number to see if there's anything else...

print read_unreal(2123456743)

# It result is:
# [2123456712, 2123456743, 'and it is hiding at 1152983631.\n']
# The value at 1152983631 is some binary zip data.

data = read_unreal(1152983631)[2]
fp = open('invader.zip', 'wb')
fp.write(data)
fp.close()

# Now unzip the file with the password "redavni" and you'll get two files:
# readme.txt
# package.pack

# readme.txt says:

# Yes! This is really level 21 in here. 
# And yes, After you solve it, you'll be in level 22!
# 
# Now for the level:
# 
# * We used to play this game when we were kids
# * When I had no idea what to do, I looked backwards.
