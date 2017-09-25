#!/usr/bin/env python3
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/def/channel.html
# There's a zipper... try getting channel.zip? And then use the zipfile library?

import io
import requests
import zipfile

response = requests.get('http://www.pythonchallenge.com/pc/def/channel.zip')
zfp = zipfile.ZipFile(io.BytesIO(response.content))

# The zip file contains a readme.txt file. It says to start from 90052.
nothing = 90052
files = {zo.filename: zo for zo in zfp.filelist}

# There are characters in the comment of each file. Looks like we might need to
# concatenate them together in the order of the nothings...

comments = []
while True:
    zip_file = files[f'{nothing}.txt']
    comments.append(zip_file.comment.decode('utf-8'))
    with zfp.open(zip_file) as fp:
        data = fp.read().decode('utf-8')
    if data.startswith('Next nothing is '):
        nothing = int(data.split()[-1])
    else:
        break

print(data)
print(''.join(comments))

# The result is an ascii picture that says HOCKEY using the letter OXYGEN.
# That must be what the title of the page referrs to (now there are pairs).

# If you go to: http://www.pythonchallenge.com/pc/def/hockey.html, it says
# that "it's in the air. look at the letters.".

# Go to: http://www.pythonchallenge.com/pc/def/oxygen.html
