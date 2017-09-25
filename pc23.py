#!/usr/bin/env python3
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/hex/bonus.html

# There a picture of a cow

# Page title is "what is this module?"

# There's a header comment:
# TODO: do you owe someone an apology? now it is a good time to
# tell him that you are sorry. Please show good manners although
# it has nothing to do with this level.

# Another comment after bonus.jpg:
# it can't find it. this is an undocumented module.

# And one last footer comment:
# 'va gur snpr bs jung?'

# We can attempt a simple Caesar cipher decryption on 'va gur snpr bs jung?'
# We find that if we shift the characters 13 steps forwards, precisely halfway
# through the alphabet, we get 'in the face of what?'

def caesar_shift(c, offset=0):
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return chr((ord(c) - 97 + offset) % 26 + 97)
    return c

print(''.join([caesar_shift(c, 13) for c in 'va gur snpr bs jung?']))

# The header comment suggests we owe someone an apology. In level 19, the wav
# file encoded in the email from leopold.moz@pythonchallenge.com contained the
# word "sorry".

# If you go to: http://www.pythonchallenge.com/pc/hex/sorry.html
# it responds: - "what are you apologizing for?"

# If you send an email to leopold.moz@pythonchallenge.com
# Subject: sorry

# You get a response:

# From: "Leopold Mozart" <leopold.moz@pythonchallenge.com>
# To: shadanan@gmail.com
# Subject: Re: my broken zip
#
# Never mind that.
# Have you found my broken zip?
# md5: bbb8b499a0eef99b52c7f13f4e78c24b
# Can you believe what one mistake can lead to?

# So far:
# apology for leopold
# broken zip file (where is the broken zip file?)
# Can you believe what one mistake can lead to? (what mistake?)
# what is this module? (presumably it is undocumented)
# in the face of what? (evil?, danger?)
# it can't find it (what's it?)

print(''.join([caesar_shift(c, 13) for c in 'bonus']))

import vg
