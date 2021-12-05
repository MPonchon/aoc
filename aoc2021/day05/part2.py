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
debug_list= []

def check_coord_diag(x, y, xl0, yl0, xl1, yl1) -> bool:
    if xl1 == xl0:
        # raise ValueError("deja traité")
        if not check_one_coord(y, yl0, yl1):
            return False
        return True

    # msg = f"check_coord_diag {x}, {y};"
    # debug_list.append(msg)
    if not check_one_coord(x, xl0, xl1):
        return False

    if not check_one_coord(y, yl0, yl1):
        return False

    a = (yl1-yl0)/(xl1 -xl0)
    b = yl0 - a*xl0
    # print(f"a:{a}, b{b}.")

    # msg = f"{x}, {y}, a: {a} ; b: {b}"
    # debug_list.append(msg)
    if y == a * x + b:
        return True


    return False




def point_in_line_xy(x, y, xl0, yl0, xl1, yl1) -> bool:

    # print("check x")
    if not check_coord_x(x, y, xl0, yl0, xl1, yl1):
        return False
# 
    # print("check y")
    if not check_coord_y(x, y, xl0, yl0, xl1, yl1):
        return False

    # print("check diag")
    if not check_coord_diag(x, y, xl0, yl0, xl1, yl1):
        return False

    # print("check false")
    return True


def compute_points(thlines: list, xmax, ymax):
    points = {}
    

    for thline in thlines:
        # for x in range(thline[0][0], thline[1][0] + 1):
        for x in range(0, xmax + 1):
            if not check_one_coord(x, thline[0][0], thline[1][0]):
                continue
            inside = False
            for y in range(0, ymax + 1):
                if not check_one_coord(y, thline[0][1], thline[1][1]):
                    continue

                key = f"{x}#{y}"

                # print(f"{x}, {y}, thline: {thline}")
                # print(f" point({x}, {y} ? in {thline}.")
                inside = False
                # if point_in_line((x,y), thline):
                if point_in_line_xy(x, y, thline[0][0], thline[0][1], thline[1][0] ,thline[1][1]):
                    inside = True
                    if key not in points:
                        points[key] = 1
                    else:
                        points[key] += 1
                    # print(f" point({x}, {y}: in {thline}. c:{points[key]}.")

    #             msg = f"{x}, {y}, thline: {thline} ; inside: {inside}"
    #             debug_list.append(msg)
    # with open("debug2-th-part2.1.txt", "w+") as f:
    #     for line in debug_list:
    #         f.write(line + '\n')
    return points

if __name__ == "__main__":
    print("AOC: part2")

    # get data
    path_to_file = os.path.join(os.getcwd(), 'data.txt')
    # path_to_file = os.path.join(os.getcwd(), 'exemple.txt')
    data = loader.load_data(path_to_file)

    # thlines = get_thlines(data, True)
    thlines = get_thlines(data, False)
    xmax, ymax = get_maxi(thlines)
# 
    # xmax = ymax = 200
    
    print(f"xmax: {xmax}, ymax:{ymax}.")
    print(f"nb lines: {len(thlines)}.")


    start = time.time()
    points = compute_points(thlines, xmax, ymax)
    print(points)
    end = time.time()
    elapsed = end - start

    print(f"elapsed:{elapsed}. ")

    tot = count_max_point(points)
    print(f"nb points: {tot}.")

    # part1
    # nb points: 5608.      elapsed:13.833225965499878.

    # 200 : 70          9.30        0.29
    # 150 : 7   , time: 5.16
    # 100 : 2           2.26

    # part2
    # elapsed:178.14009428024292. 
    # nb points: 20299.