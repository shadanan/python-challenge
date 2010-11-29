#!/usr/bin/env python
# encoding: utf-8

encoded = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc d" \
    "mp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm j" \
    "mle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

def decode(char):
    if char in (' ', '.'):
        return char
    return chr((ord(char) - ord('a') + 2) % 26 + ord('a'))

print "".join(map(decode, encoded))
print
print "".join(map(decode, "map"))