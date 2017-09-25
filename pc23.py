#!/usr/bin/env python3
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/hex/bonus.html

# There a picture of a cow

# Page title is "what is this module?"

# Comment after bonus.jpg:
# it can't find it. this is an undocumented module.

# And one last footer comment:
# 'va gur snpr bs jung?'

# this is *literally* an undocumented module
import re
import this

# We can decode 'va gur snpr bs jung?' using the encoding provided in this.d:
print(''.join([this.d.get(c, c) for c in 'va gur snpr bs jung?']))
# Result is: 'in the face of what?'

# When you import this, it prints out the zen of python.
zen = ''.join(this.d.get(c, c) for c in this.s)

# The line starting with 'In the face of' is: ambiguity
print(re.findall(r'In the face of ([a-z]+)', zen)[0])

# Next level: http://www.pythonchallenge.com/pc/hex/ambiguity.html


# There's a header comment:
# TODO: do you owe someone an apology? now it is a good time to
# tell him that you are sorry. Please show good manners although
# it has nothing to do with this level.

# The header comment suggests we owe someone an apology. In level 19, the wav
# file encoded in the email from leopold.moz@pythonchallenge.com contained the
# word "sorry".

# If you go to: http://www.pythonchallenge.com/pc/hex/sorry.html
# it responds: - "what are you apologizing for?"

# After you complete level 19, when you visit:
# http://www.pythonchallenge.com/pc/hex/idiot.html
# It says, "Now you should apologize..." under a picture of Leopold Mozart

# If you send an email to leopold.moz@pythonchallenge.com
# Subject: sorry

# You get a response:

# From: "Leopold Mozart" <leopold.moz@pythonchallenge.com>
# To: shadanan@gmail.com
# Subject: Re: my broken zip

# Never mind that.
# Have you found my broken zip?
# md5: bbb8b499a0eef99b52c7f13f4e78c24b
# Can you believe what one mistake can lead to?

# So, we're not there yet, but at some point, we need to find Leopold's broken
# zip file.
