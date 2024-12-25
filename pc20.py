#!/usr/bin/env python3
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/hex/idiot2.html
# username: butter, password: fly

# If you look at the response headers for unreal.jpg, we notice that there's
# a suspicious: "Content-Range: bytes 0-30202/2123456789"

# If you try to ask for data beyond 30202, you get:
# "Why don't you respect my privacy?"
# Maybe we should read even further ahead? Perhaps loop over the end value?

import io
import zipfile

import httpx


def read_unreal(start, stop=""):
    response = httpx.get(
        "http://www.pythonchallenge.com/pc/hex/unreal.jpg",
        auth=("butter", "fly"),
        headers={"Range": f"bytes={start}-{stop}"},
    )

    if "Content-Range" not in response.headers:
        return None

    nrange = response.headers["Content-Range"]
    x, y = nrange.split(" ")[1].split("/")[0].split("-")
    return int(x), int(y), response.content


pos = 30203
while True:
    curr = read_unreal(pos)
    if curr is None:
        break
    print(curr)
    pos = curr[1] + 1

# The result is:
# (30203, 30236, b"Why don't you respect my privacy?\n")
# (30237, 30283, b'we can go on in this way for really long time.\n')
# (30284, 30294, b'stop this!\n')
# (30295, 30312, b'invader! invader!\n')
# (30313, 30346, b'ok, invader. you are inside now. \n')

# If we visit: http://www.pythonchallenge.com/pc/hex/invader.html
# We get: "Yes! that's you!"

# Let's try reading from 2123456789

print(read_unreal(2123456789))

# The result is:
# (2123456744, 2123456788, b'esrever ni emankcin wen ruoy si drowssap eht\n')
# That is, 'the password is your new nickname in reverse'. It must mean
# 'invader' backwards ('redavni')
# Let's try going down a number to see if there's anything else...

print(read_unreal(2123456743))

# The result is:
# (2123456712, 2123456743, b'and it is hiding at 1152983631.\n')
# The value at 1152983631 is some binary zip data.

data = read_unreal(1152983631)
assert data is not None
zf = zipfile.ZipFile(io.BytesIO(data[2]))

# Now list files in the zip file:

print("\n".join([x.filename for x in zf.filelist]))

# readme.txt
# package.pack

# And if we read readme.txt, it says:

with zf.open("readme.txt", pwd=b"redavni") as fp:
    print(fp.read().decode("utf-8"))

# Yes! This is really level 21 in here.
# And yes, After you solve it, you'll be in level 22!
#
# Now for the level:
#
# * We used to play this game when we were kids
# * When I had no idea what to do, I looked backwards.
