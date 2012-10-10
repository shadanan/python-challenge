#!/usr/bin/env python
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/def/channel.html
# There's a zipper... try getting channel.zip? And then use the zipfile library?
import zipfile
import os

fp = zipfile.ZipFile('channel.zip')

# The zip file contains a readme.txt file. It says to start from 90052.

nothing = 90052

files = {}
for zo in fp.filelist:
    files[zo.filename] = zo

def read_zip_file(fp, zip_file):
    file_path = fp.extract(zip_file)
    fp = open(file_path, 'r')
    data = fp.read()
    os.unlink(file_path)
    return data

# There are characters in the comment of each file. Looks like we might need to 
# concatenate them together in the order of the nothings...

comment = []
while True:
    zip_file = files['%s.txt' % nothing]
    comment.append(zip_file.comment)
    data = read_zip_file(fp, zip_file)
    if data.startswith("Next nothing is "):
        nothing = int(data.split()[-1])
    else:
        break

print data
print "".join(comment)

# The result is an ascii picture that says HOCKEY using the letter OXYGEN.
# That must be what the title of the page referrs to (now there are pairs).

# If you go to: http://www.pythonchallenge.com/pc/def/hockey.html, it says
# that "it's in the air. look at the letters.".

# Go to: http://www.pythonchallenge.com/pc/def/oxygen.html