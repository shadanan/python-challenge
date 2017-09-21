#!/usr/bin/env python3

# Start at: http://www.pythonchallenge.com/pc/return/bull.html

# The source contains "a = [1, 11, 21, 1211, 111221, "
# and asks for len(a[30])... so we need to find out what the
# length of the 30th element would be. The pattern is pretty
# self evident. Just say it out loud.

a = ['1', '11', '21', '1211', '111221']

while len(a) != 31:
    val = a[-1][0]
    count = 0
    curr = []

    for x in a[-1]:
        if val == x:
            count += 1
        else:
            curr.append(str(count))
            curr.append(val)
            val = x
            count = 1

    curr.append(str(count))
    curr.append(val)
    a.append(''.join(curr))

print(len(a[30]))

# Result is 5808.
# Go to: http://www.pythonchallenge.com/pc/return/5808.html
