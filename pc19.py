#!/usr/bin/env python3
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/hex/bin.html
# username: butter, password: fly

# You get a picture of india, and base64 encoded email in the HTML source
# If you go to: http://www.pythonchallenge.com/pc/hex/india.html
# it responds: "nnn. what could this mean?"

# Let's read the email in and decode it.

import email.parser
import io
import tempfile
import wave
from email.mime.multipart import MIMEMultipart
from typing import cast

import httpx

response = httpx.get(
    "http://www.pythonchallenge.com/pc/hex/bin.html", auth=("butter", "fly")
)
data = response.text

# According to the MIME type, the encoded data is a WAV file
parser = email.parser.Parser()
message = parser.parsestr(data[data.find("<!--") + 5 : data.find("-->")])

attachment = cast(list[MIMEMultipart], message.get_payload())
original_wav = cast(bytes, attachment[0].get_payload(decode=True))

with tempfile.NamedTemporaryFile(mode="wb", suffix=".wav", delete=False) as fp:
    fp.write(original_wav)
    print(f"Original: {fp.name}")

# The decoded file is a bunch of static with a single word: "sorry"

# Let's try modifying the properties of the audio file.

# The original number of channels was 1 -- perhaps there's something encoded
# in a second channel? In that case, let's change the sample width to 1
# so that we double the amount of data points (first half of short becomes
# the left channel and second half become the right channel)

with (
    tempfile.NamedTemporaryFile(mode="wb", suffix=".wav", delete=False) as fp,
    wave.open(io.BytesIO(original_wav)) as fp_r,
    wave.open(fp, "wb") as fp_w,
):
    fp_w.setnchannels(2)
    fp_w.setsampwidth(1)
    fp_w.setframerate(fp_r.getframerate())
    fp_w.writeframes(fp_r.readframes(fp_r.getnframes()))
    print(f"Corrected: {fp.name}")

# Open the corrected file and you hear "you are an idiot"
# Go to: http://www.pythonchallenge.com/pc/hex/idiot.html
# It says, "Now you should apologize..." with a link to the next level
