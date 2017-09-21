#!/usr/bin/env python3
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/return/uzi.html

# Page title is "whom?" and comments in HTML source code are:
# "he ain't the youngest, he is the second" and
# "todo: buy flowers for tomorrow"

# The image is a calendar with the month January, 1*6. The 26th of the month
# is a Monday. The February list in the bottom show that it's a leap year.
# I think we need to find the year that matches these constraints.

import datetime

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
for i in range(99, 0, -1):
    year = int(f'1{i}6')
    d = datetime.datetime(year, 1, 26)
    if d.weekday() == 0 and is_leap_year(year):
        valid_dates.append(d)

print(valid_dates[1])

# The year that matches is 1756.
# What's special about the day after January 26th, 1756? Check google:
# Aha, mozart was born on that day!
# Go to: http://www.pythonchallenge.com/pc/return/mozart.html
