#!/usr/bin/env python3
# https://adventofcode.com/
# part1.py

from utils import loader
import os

import time
"""
--- Day 5: Hydrothermal Venture ---

You come across a field of hydrothermal vents on the ocean floor! 
These vents constantly produce large, opaque clouds, so 
it would be best to avoid them if possible.

They tend to form in lines; the submarine helpfully produces 
a list of nearby lines of vents (your puzzle input) f

or you to review. For example:

0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2

Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 
where x1,y1 are the coordinates of one end the line segment 
and x2,y2 are the coordinates of the other end. 

These line segments include the points at both ends. 

In other words:
    An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
    An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.

For now, only consider horizontal and vertical lines: 
lines where either x1 = x2 or y1 = y2.

So, the horizontal and vertical lines from the above list 
would produce the following diagram:

    0,0             9,0
        .......1..
        ..1....1..    1.2  in  1,2-> 1,3
        ..1....1..
        .......1..
   0,4 .112111211
        ..........
        ..........
        ..........
        ..........
        222111....
    0,9             9,9

In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. 
Each position is shown as the number of lines which cover that point
 or .if no line covers that point. 
 The top-left pair of 1s, 
 for example, comes from 2,2 -> 2,1; 
 the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.

To avoid the most dangerous areas, you need to determine the number of points 
where at least two lines overlap. 
In the above example, this is anywhere in the diagram with a 2 or larger 
- a total of 5 points.

Consider only horizontal and vertical lines. 
At how many points do at least two lines overlap?


"""

def normalize_x(tup0, tup1):
    if tup0[0] > tup1[0]:
        return (tup1, tup0)
    return (tup0, tup1)


def get_thlines(lines: list, filtreHV) -> list:

    def tupize(entree: str):
        x, y = entree.split(',')
        return (int(x.strip()), int(y.strip()))

    mydata = []
    for line in lines:
        parts = line.split('->')
        tup0 = tupize(parts[0]) 
        tup1 = tupize(parts[1])

        tup = normalize_x(tup0, tup1)

        # tup = (tupize(parts[0]), tupize(parts[1]))
        if filtreHV:
            if tup[0][0] != tup[1][0] and tup[0][1] != tup[1][1]:
                continue
        mydata.append(tup)
    return mydata

def get_maxi(thlines: list):
    xmax = ymax = 0
    for thline in thlines:
        xmax = max(xmax, thline[0][0], thline[1][0])
        ymax = max(ymax, thline[0][1], thline[1][1])
    return xmax, ymax

def check_coord_x(x, y, xl0, yl0, xl1, yl1):
    # print(f"check_coord_x: {x}, {y}  ({xl0}, {yl0}) -> ({xl1}, {yl1})")
    return check_coord(x, y, xl0, yl0, xl1, yl1)

def check_coord_y(x, y, xl0, yl0, xl1, yl1):
    # print(f"check_coord_y: {x}, {y}  ({xl0}, {yl0}) -> ({xl1}, {yl1})")
    return check_coord(y, x, yl0, xl0, yl1, xl1)

def check_coord(x, y, xl0, yl0, xl1, yl1):
    # print(f"check_coord: {x}, {y}  ({xl0}, {yl0}) -> ({xl1}, {yl1})")

    if not check_one_coord(x, xl0, xl1):
        return False

    if not check_one_coord(y, yl0, yl1):
        return False

    return True


def check_one_coord(x, x0, x1):
    if x1 < x0:
        return check_one_coord(x, x1, x0)
    return x >= x0 and x <= x1


def point_in_line(point: tuple, line: tuple) -> bool:
    x = point[0]
    y = point[1]

    xl0 = line[0][0]
    yl0 = line[0][1]
    xl1 = line[1][0]
    yl1 = line[1][1]

    return point_in_line_xy(x, y, xl0, yl0, xl1, yl1)
    # # print(f"point_in_line: {x}, {y}  ({xl0}, {yl0}) -> ({xl1}, {yl1})")
    # # print("check x")
    # if not check_coord_x(x, y, xl0, yl0, xl1, yl1):
    #     return False

    # # print("check y")
    # if not check_coord_y(x, y, xl0, yl0, xl1, yl1):
    #     return False

    # # print("check false")
    # return True

def point_in_line_xy(x, y, xl0, yl0, xl1, yl1) -> bool:

    if not check_coord_x(x, y, xl0, yl0, xl1, yl1):
        return False

    # print("check y")
    if not check_coord_y(x, y, xl0, yl0, xl1, yl1):
        return False


    # print("check false")
    return True

def compute_points(thlines: list, xmax, ymax):
    points = {}
    debug_list= []

    for thline in thlines:
        # for x in range(thline[0][0], thline[1][0] + 1):
        for x in range(0, xmax + 1):
            if not check_one_coord(x, thline[0][0], thline[1][0]):
                continue
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
                #     # print(f" point({x}, {y}: in {thline}. c:{points[key]}.")
                # else:
                #     # print(f" point({x}, {y} NOT in {thline}.")
                #     pass
                msg = f"{x}, {y}, thline: {thline} ; inside: {inside}"
                debug_list.append(msg)
    with open("debug-th-part1.txt", "w+") as f:
        for line in debug_list:
            f.write(line + '\n')
    return points


def count_max_point(points: dict) -> int:
    tot = 0
    for key, count in points.items():
        # print(f"key:{key}, count{count}.")
        if count > 1:
            # print(f"key:{key}")
            tot += 1
    return tot


if __name__ == "__main__":
    print("AOC: part1")

    # get data
    path_to_file = os.path.join(os.getcwd(), 'data.txt')
    # path_to_file = os.path.join(os.getcwd(), 'exemple.txt')
    data = loader.load_data(path_to_file)

    thlines = get_thlines(data, True)
    xmax, ymax = get_maxi(thlines)

    xmax = ymax = 200
    
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
    # nb points: 5608.      elapsed:13.833225965499878.

    # 200 : 70          9.30        0.028
    # 150 : 7   , time: 5.16
    # 100 : 2           2.26

