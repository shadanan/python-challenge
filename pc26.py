#!/usr/bin/env python3
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/hex/decent.html

# It's a picture of a couple of indecent monkeys
# Captioned with: "Hurry up, I'm missing the boat"
# The page title is: "be a man - apologize!"
# There a single comment: "you've got his email"

# I'm pretty sure that this is the level where we solve Leopold's broken zip.
# Here's the background, collected from the previous levels:

# In level 19, the wav file encoded in the email from
# leopold.moz@pythonchallenge.com contained the word "sorry".
# If you go to: http://www.pythonchallenge.com/pc/hex/sorry.html
# it responds: - "what are you apologizing for?"

# After you complete level 19, when you visit:
# http://www.pythonchallenge.com/pc/hex/idiot.html
# It says, "Now you should apologize..." under a picture of Leopold Mozart

# In level 23, there's was a header comment:
# TODO: do you owe someone an apology? now it is a good time to
# tell him that you are sorry. Please show good manners although
# it has nothing to do with this level.
# The header comment suggests we owe someone an apology.

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

# In level 24, the resulting zip file contained mybroken.zip.

import hashlib
import io
import zipfile

from PIL import Image

import pc24

# Read zip data
with pc24.zf.open("mybroken.zip") as fp:
    broken = fp.read()


# The email from Leopold contains an md5 hex digest. Try repairing the zip file
# assuming that one of the bytes is incorrect.
def repair(data, md5):
    for i in range(len(data)):
        data_array = bytearray(data)
        for j in range(256):
            data_array[i] = j
            if hashlib.md5(data_array).hexdigest() == md5:
                return data_array
    raise Exception("Failed to repair")


fixed = repair(broken, "bbb8b499a0eef99b52c7f13f4e78c24b")

# There's only one file in the archive.
bzf = zipfile.ZipFile(io.BytesIO(fixed))
with bzf.open("mybroken.gif") as fp:
    data = fp.read()

# The image shows the word "speed"
image = Image.open(io.BytesIO(data))
image.show()

# If you try to go to speed.html, you get 404. Recalling that the caption for the level
# is "Hurry up, I'm missing the boat", try speedboat instead.

# Go to: http://www.pythonchallenge.com/pc/hex/speedboat.html
