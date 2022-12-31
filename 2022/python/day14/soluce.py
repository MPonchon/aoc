# https://blurt.blog/adventofcode/@justyy/avent-of-code-day-14-regolith-reservoir


import sys
from collections import defaultdict, deque
from math import inf
from icecream import ic

file_data = "exemple.txt"
# file_data = "input.txt"


file1 = open(file_data, "r")

grid = defaultdict(lambda: ".")
sand = (500, 0)
minx = sand[0]
maxx = sand[0]
miny = sand[1]
maxy = sand[1]


def show(grid):
    for l in range(miny, maxy +1):
        line = f"{l:4} "
        for c in range(minx, maxx +1):
            # ic(c)
            val = grid[(c, l)]
            line += val
            # ic (c, l, val)
            # if val == '#':
            #     line += '#'
            # elif val == '.':
            #     line += "o"
            # elif val == '.':
            #     line += "."
            # else:
            #     line +=  "-"
        ic (line)



while True:
    line = file1.readline()
    if not line:
        break
    line = line.strip()
    arr = line.split("->")
    prev = None
    for s in arr:
        a, b = map(int, s.split(","))
        minx = min(minx, a)
        maxx = max(maxx, a)
        miny = min(miny, b)
        maxy = max(maxy, b)
        ic(maxx)
        grid[(a, b)] = "#"
        if prev:
            if a == prev[0]:
                for x in range(min(b, prev[1]), max(b, prev[1]) + 1):
                    grid[(a, x)] = "#"
            elif b == prev[1]:
                for x in range(min(a, prev[0]), max(a, prev[0]) + 1):
                    grid[(x, b)] = "#"
        prev = (a, b)


ans = 0

print(minx, maxx, miny, maxy)
show(grid)

while True:
    x, y = sand
    settled = False
    while minx <= x <= maxx and miny <= y <= maxy:
        if grid[(x, y + 1)] == ".":
            y += 1
        elif grid[(x + 1, y + 1)] != "." and grid[(x - 1, y + 1)] != ".":
            grid[(x, y)]= "o"
            ans += 1
            settled = True
            break
        elif grid[(x - 1, y + 1)] == ".":
            y += 1
            x -= 1
        else:
            y += 1
            x += 1
    if not settled:
        break
show(grid)
print(f"ans:{ans}")
