#!/usr/bin/env python3
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/return/good.html
# un: huge, pw: file

# Source of the page says first+second=? and contains:
# The image reminds me of connect the dots. So, let's connect the dots...

import httpx
from PIL import Image, ImageDraw

type Coordinate = tuple[int, int]


def parse_coords(label: str) -> list[Coordinate]:
    start = lines.index(label)
    end = lines.index("", start)
    csv = "".join(lines[start + 1 : end])
    values = [int(v) for v in csv.split(",")]
    return list(zip(values[0::2], values[1::2]))


response = httpx.get(
    "http://www.pythonchallenge.com/pc/return/good.html", auth=("huge", "file")
)
lines = response.text.strip().splitlines()
first = parse_coords("first:")
second = parse_coords("second:")

image = Image.new("RGB", (500, 500))
draw = ImageDraw.Draw(image)
draw.line(first, fill="white")
draw.line(second, fill="white")
image.show()

# Looks like a picture of a bull...
# Go to: http://www.pythonchallenge.com/pc/return/bull.html
