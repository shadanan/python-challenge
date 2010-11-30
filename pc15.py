#!/usr/bin/env python
# encoding: utf-8

import datetime
import pcutils

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

valid_dates = []
for i in xrange(99, 0, -1):
    year = int("1%d6" % i)
    d = datetime.datetime(year, 1, 26)
    if d.weekday() == 0 and is_leap_year(year):
        valid_dates.append(d)

print valid_dates[1]
