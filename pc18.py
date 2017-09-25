#!/usr/bin/env python3
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/return/balloons.html

# Can you tell the difference? It is the brightness...
# Go to: http://www.pythonchallenge.com/pc/return/brightness.html

# Source says: maybe consider deltas.gz

import difflib
import gzip
import requests
import tempfile

response = requests.get('http://www.pythonchallenge.com/pc/return/deltas.gz',
                        auth=('huge', 'file'))
data = gzip.decompress(response.content).decode('utf-8')

# The file contains two sequences of lines... separate them.
left = [x.split('   ')[0] for x in data.splitlines()]
right = [x.split('   ')[1] for x in data.splitlines()]

# Looks like they are similar, but different. Separate into three streams,
# one for what's equal, one with the left and one with the right.
with tempfile.NamedTemporaryFile(mode='wb', suffix='.png', delete=False) as fp1, \
        tempfile.NamedTemporaryFile(mode='wb', suffix='.png', delete=False) as fp2, \
        tempfile.NamedTemporaryFile(mode='wb', suffix='.png', delete=False) as fp3:
    for x in difflib.ndiff(left, right, charjunk=None):
        # print(x)
        if x.startswith('  '):
            fp1.write(bytes([int(x, 16) for x in x[2:].split()]))
        elif x.startswith('- '):
            fp2.write(bytes([int(x, 16) for x in x[2:].split()]))
        elif x.startswith('+ '):
            fp3.write(bytes([int(x, 16) for x in x[2:].split()]))

    print(f'Next: {fp1.name}, User: {fp3.name}, Pass: {fp2.name}')

# Go to: http://www.pythonchallenge.com/pc/hex/bin.html
# User: butter, Pass: fly
