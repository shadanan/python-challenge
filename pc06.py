#!/usr/bin/env python
# encoding: utf-8

import zipfile
import os

# Initial nothing found in readme.txt
nothing = 90052

fp = zipfile.ZipFile('channel.zip')

files = {}
for zo in fp.filelist:
    files[zo.filename] = zo

def read_zip_file(fp, zip_file):
    file_path = fp.extract(zip_file)
    fp = open(file_path, 'r')
    data = fp.read()
    os.unlink(file_path)
    return data

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