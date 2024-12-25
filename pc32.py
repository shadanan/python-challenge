#!/usr/bin/env python3
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/rock/arecibo.html
# User: kohsamui, Pass: thailand

# JavaScript app of a picross game
# Page title: "etch-a-sketch"
# Caption: "Fill in the blanks"
# Comment in HTML: "<!-- for warmup.txt -->"

# The warmup.txt file contains a small 9x9 picross.
# Solving by hand reveals an up arrow.

# Go to: http://www.pythonchallenge.com/pc/rock/up.html
# User: kohsamui, Pass: thailand

# We are presented with a new caption:
# You want to go up? Let's scale this up then. Now get serious and solve this.
# Links to a much harder 32x32 picross. Let's write a solver.

import itertools
from typing import NamedTuple

import numpy as np
import requests
from numpy.typing import NDArray
from PIL import Image


class Rules(NamedTuple):
    rows: list[tuple[int, ...]]
    cols: list[tuple[int, ...]]


def parse_rules(text: str) -> Rules:
    rules = Rules([], [])
    state = 0
    for line in text.splitlines():
        if line == "":
            pass
        elif line.startswith("# Horizontal"):
            state = 1
        elif line.startswith("# Vertical"):
            state = 2
        elif state == 1:
            rules.rows.append(tuple(int(v) for v in line.split()))
        elif state == 2:
            rules.cols.append(tuple(int(v) for v in line.split()))
    return rules


# Generates the possible spacings between runs of a line.
def spacings(length: int, clues: tuple[int, ...]):
    groups = len(clues)
    spaces = length - sum(clues) + 1
    cumsum = list(itertools.chain([0], itertools.accumulate(clues)))
    for comb in itertools.combinations(range(spaces), groups):
        yield tuple(sum(z) for z in zip(comb, cumsum))


# Generates all possible lines given the current constraints.
def possible_lines(clues: tuple[int, ...], constraint: NDArray):
    results = []
    for offsets in spacings(len(constraint), clues):
        result = np.ones(len(constraint), dtype=np.int8) * -1
        for offset, clue in zip(offsets, clues):
            result[offset : clue + offset] = 1
        if 0 not in np.array([result, constraint]).sum(axis=0):
            results.append(result)
    return np.array(results)


# Finds forcing elements for a set of all possible lines.
def update_constraint(clues: tuple[int, ...], constraint: NDArray):
    lines = possible_lines(clues, constraint)
    nc = len(lines)
    ls = lines.sum(axis=0)
    return np.where(ls == nc, 1, 0) + np.where(ls == -nc, -1, 0)


# This function renders an image from the current nonogram state.
def render(nonogram: NDArray, scale: int = 10):
    img = Image.fromarray((nonogram + 1), mode="P")
    img.putpalette([0, 0, 0, 127, 127, 127, 255, 255, 255])
    return img.resize([i * scale for i in img.size])


# Solve the nonogram given a set of rules.
def solve(rules: Rules):
    nonogram = np.zeros((len(rules.rows), len(rules.cols)), dtype=np.int8)
    yield nonogram
    while 0 in nonogram:
        prev_nonogram = nonogram.copy()
        for row in range(nonogram.shape[0]):
            nonogram[row, :] = update_constraint(rules.rows[row], nonogram[row, :])
            yield nonogram
        for col in range(nonogram.shape[1]):
            nonogram[:, col] = update_constraint(rules.cols[col], nonogram[:, col])
            yield nonogram
        if (prev_nonogram == nonogram).all():
            raise Exception("No change after iterating all rows and cols")


def save_animation(frames: list[Image.Image], name: str, duration: int = 60):
    frames[0].save(
        name,
        format="GIF",
        append_images=frames[1:],
        save_all=True,
        duration=duration,
        loop=0,
    )


# Test the solver on the warmup puzzle.
response = requests.get(
    "http://www.pythonchallenge.com/pc/rock/warmup.txt",
    auth=("kohsamui", "thailand"),
)
rules = parse_rules(response.text)
frames = [render(n) for n in solve(rules)]
frames[-1].show()
save_animation(frames, "warmup.gif")

# Run the solver on the larger puzzle.
response = requests.get(
    "http://www.pythonchallenge.com/pc/rock/up.txt",
    auth=("kohsamui", "thailand"),
)
rules = parse_rules(response.text)
frames = [render(n) for n in solve(rules)]
frames[-1].show()
save_animation(frames, "up.gif")

# The result is a picture of a snake, probably a python?

# Go to: http://www.pythonchallenge.com/pc/rock/python.html
# User: kohsamui, Pass: thailand

# We see the python image we generated.
# The title of the page is: "here we go"
# The caption is:
# Congrats! You made it through to the smiling python.
# "Free" as in "Free speech", not as in "free...

# Go to: http://www.pythonchallenge.com/pc/rock/beer.html
# User: kohsamui, Pass: thailand
