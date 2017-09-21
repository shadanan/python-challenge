#!/usr/bin/env python3
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/hex/bin.html
# username: butter, password: fly

# You get a picture of india, and base64 encoded email in the HTML source
# If you go to: http://www.pythonchallenge.com/pc/hex/india.html
# it responds: "nnn. what could this mean?"

# Let's read the email in and decode it.

import email
import io
import urllib.request
import wave

password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(realm=None,
                          uri='http://www.pythonchallenge.com/pc/hex/',
                          user='butter',
                          passwd='fly')
auth_handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

opener = urllib.request.build_opener(auth_handler)
with opener.open('http://www.pythonchallenge.com/pc/hex/bin.html') as fp:
    data = fp.read().decode('utf-8')

# According to the MIME type, the encoded data is a WAV file
parser = email.parser.Parser()
message = parser.parsestr(data[data.find('<!--')+5:data.find('-->')])

attachment = message.get_payload()[0]
original_wav = attachment.get_payload(decode=True)

with open('indian_original.wav', 'wb') as fp:
    fp.write(original_wav)

# The decoded file is a bunch of static with a single word: "sorry"
# If you go to: http://www.pythonchallenge.com/pc/hex/sorry.html
# it responds: - "what are you apologizing for?"

# Try sending an email to leopold.moz@pythonchallenge.com
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

# Let's try modifying the properties of the audio file.

fp_r = wave.open(io.BytesIO(original_wav))
fp_w = wave.open('indian_corrected.wav', 'wb')

# The original number of channels was 1 -- perhaps there's something encoded
# in a second channel? In that case, let's change the sample width to 1
# so that we double the amount of data points (first half of short becomes
# the left channel and second half become the right channel)
fp_w.setnchannels(2)
fp_w.setsampwidth(1)
fp_w.setframerate(fp_r.getframerate())
fp_w.writeframes(fp_r.readframes(fp_r.getnframes()))

fp_r.close()
fp_w.close()

# Open the file 'indian_corrected.wav' and you hear "you are an idiot"
# Go to: http://www.pythonchallenge.com/pc/hex/idiot.html
# It says, "Now you should apologize..." with a link to the next level
