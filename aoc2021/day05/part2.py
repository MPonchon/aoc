#!/usr/bin/env python3
# https://adventofcode.com/
# part2.py

"""
-- Part Two ---

Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture; you need to also consider diagonal lines.

Because of the limits of the hydrothermal vent mapping system, the lines in your list will only ever be horizontal, vertical, or a diagonal line at exactly 45 degrees. In other words:

    An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
    An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.

Considering all lines from the above example would now produce the following diagram:

1.1....11.
.111...2..
..2.1.111.
...1.2.2..
.112313211
...1.2....
..1...1...
.1.....1..
1.......1.
222111....

You still need to determine the number of points where at least two lines overlap. In the above example, this is still anywhere in the diagram with a 2 or larger - now a total of 12 points.

Consider all of the lines. At how many points do at least two lines overlap?
"""
from utils import loader
import os

from part1 import *

def calcul1():
    pass

if __name__ == "__main__":
    print("AOC: part2")

    # get data
    path_to_file = os.path.join(os.getcwd(), 'data.txt')
    # path_to_file = os.path.join(os.getcwd(), 'exemple.txt')
    data = loader.load_data(path_to_file)

    thlines = get_thlines(data, False)

    xmax, ymax = get_maxi(thlines)
    print(f"xmax: {xmax}, ymax:{ymax}.")
    print(f"nb lines: {len(thlines)}.")
    xmax = ymax = 100

    start = time.time()
    points = compute_points(thlines, xmax, ymax)
    print(points)
    end = time.time()
    elapsed = end - start

    print(f"elapsed:{elapsed}. ")

    tot = count_max_point(points)
    print(f"nb points: {tot}.")
    # nb points: 5608.

    # # 200 : 70          9.30
    # # 150 : 7   , time: 5.16
    # # 100 : 2           2.26  -> 3.55
