#!/usr/bin/env python3
# encoding: utf-8

# Start at: http://www.pythonchallenge.com/pc/hex/ambiguity.html

# There's a png maze. The title of the page is "from top to bottom". Let's
# solve the maze!

import io
import zipfile

import httpx
from PIL import Image


class Maze:
    def __init__(self, width, height):
        self.maze = [[0] * width for _ in range(height)]

    def __getitem__(self, loc):
        return self.maze[loc[0]][loc[1]]

    def __setitem__(self, loc, item):
        self.maze[loc[0]][loc[1]] = item

    @property
    def width(self):
        return len(self.maze[0])

    @property
    def height(self):
        return len(self.maze)

    def visualize(self):
        img = Image.new("RGB", (self.width, self.height))
        for x in range(self.width):
            for y in range(self.height):
                if self[x, y] == 0:
                    img.putpixel((x, y), (255, 255, 255, 255))
                elif self[x, y] == 1:
                    img.putpixel((x, y), (0, 0, 0, 255))
                elif self[x, y] == 2:
                    img.putpixel((x, y), (47, 127, 93, 255))
                elif self[x, y] == 3:
                    img.putpixel((x, y), (200, 150, 150, 255))

        img.show()


def is_available(maze, pos):
    return (
        pos[0] >= 0
        and pos[1] >= 0
        and pos[0] < maze.width
        and pos[1] < maze.height
        and maze[pos] == 0
    )


def neighbours(pos):
    yield pos[0] - 1, pos[1]
    yield pos[0], pos[1] + 1
    yield pos[0] + 1, pos[1]
    yield pos[0], pos[1] - 1


def solve(maze, start, exit):
    path = [start]
    viables = {}

    while True:
        # If our path is empty, we didn't find a solution
        if not path:
            return None

        pos = path[-1]

        # If pos not in viables, then visit this pos for the first time
        if pos not in viables:
            maze[pos] = 2
            viables[pos] = [n for n in neighbours(pos) if is_available(maze, n)]

        # If we're at the exit, then we're done!
        if pos == exit:
            return path

        # If viables[pos] is empty, then this path is a dead end
        if not viables[pos]:
            maze[pos] = 3
            path.pop()
            continue

        # Get the next place to visit by popping it off the viables and then
        # appending it to the path
        path.append(viables[pos].pop())
        continue


# Read the maze image
response = httpx.get(
    "http://www.pythonchallenge.com/pc/hex/maze.png", auth=("butter", "fly")
)
img = Image.open(io.BytesIO(response.content))
maze = Maze(img.width, img.height)

# Convert the pixel data into maze data
for x in range(img.width):
    for y in range(img.height):
        r, g, b, _ = img.getpixel((x, y))
        if r >= 127 and g >= 127 and b >= 127:
            maze[x, y] = 1
        else:
            maze[x, y] = 0

# Find a path from the start to the exit
path = solve(maze, (639, 0), (1, 640))

# Get the red component of the color data for each point along the path
values = [img.getpixel(p)[0] for p in path]

# The even values are all zero, and the odd values end up representing zip data
zf = zipfile.ZipFile(io.BytesIO(bytearray(values[1::2])))

if __name__ == "__main__":
    # The files in the zip file are maze.jpg and mybroken.zip
    # Looks like we finally found Leopold's broken zip file!
    print("\n".join([x.filename for x in zf.filelist]))

    # maze.jpg is a picture of a lake with the word "lake" in it
    with zf.open("maze.jpg") as fp:
        Image.open(fp).show()

# Go to: http://www.pythonchallenge.com/pc/hex/lake.html
