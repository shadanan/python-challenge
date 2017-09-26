#!/usr/bin/env python3
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/hex/lake.html

# It's a picture of a calm lake with a puzzle piece overlay
# Title of the page is "imagine how they sound"
# There's a comment next to the image: "can you see the waves?"

# Well, it looks like there are files at lake{N}.wav

import io
import itertools
import requests
import tempfile
import wave


datas = []
for i in itertools.count(1):
    response = requests.get(f'http://www.pythonchallenge.com/pc/hex/lake{i}.wav',
                            auth=('butter', 'fly'))
    if response.status_code == 200:
        datas.append(response.content)
    else:
        break

waves = [wave.open(io.BytesIO(r)) for r in datas]
frames = [w.readframes(w.getnframes()) for w in waves]

fp = wave.open('output.wav', 'wb')

fp.setparams(waves[0].getparams())
# fp.setsampwidth(5)
fp.setnchannels(5)

for i in range(waves[0].getnframes()):
    for wav in waves:
        fp.writeframes(frame[i])

for frame in frames:
    fp.writeframes(frame)

fp.

fp.close()






print(waves[0].getparams())

x = zip([w.readframes(w.getnframes()) for w in waves])
next(x)

len(waves)
