#! /bin/env python3
#
# https://adventofcode.com/
#

from typing import Tuple
from icecream import ic
from collections import defaultdict
from copy import copy, deepcopy

def add_reponse(tag, reponse):
    import subprocess
    import os
    path_to_main = os.path.join(os.getcwd(), "main.py")
    if os.path.exists(path_to_main):
        command = f"sed -i 's/# {tag}.*$/# {tag}: {reponse}/g' {path_to_main}"
        subprocess.run(command, shell=True)
    else:
        ic(f"Erreur chemin: {path_to_main}")

AIR = 0
ROCK = 1
SAND = 2

class GridException(Exception):
    pass

class FallOutException(GridException):
    pass

class SandFullException(GridException):
    pass

class Grid:
    def __init__(self, lines):
        self.grid = defaultdict(lambda: AIR)
        self.xmin = self.xmax = self.ymin = self.ymax = 0
        self.create_map(lines)
        self.ymin = 0
        ic(self.xmin ,self.xmax ,self.ymin ,self.ymax )


    def _set_limits(self, x: int, y: int) -> None:
        self.xmin = min(x, self.xmin)
        self.ymin = min(y, self.ymin)
        self.xmax = max(x, self.xmax)
        self.ymax = max(y, self.ymax)


    def create_map(self, lines):
        self.xmin = self.xmax = 500
        self.ymin = self.ymax = 0
        for line in lines:
            gen_pts0 =( x.strip().split(",") for x in line.split("->"))
            gen_pts = ( ( int(x[0]),  int(x[1])) for x in gen_pts0)
            p1 = next(gen_pts)
            x , y = p1
            self._set_limits(x, y)
            for p2 in gen_pts:
                x , y = p2
                self._set_limits(x, y)
                if p1[0] == p2[0]:
                    x = p1[0] 
                    ymin = min(p1[1], p2[1])
                    ymax = max(p1[1], p2[1])
                    for y in range(ymin, ymax + 1):
                        self.grid[(x,y)] = ROCK

                elif p1[1] == p2[1]:
                    y = p1[1]
                    xmin = min(p1[0], p2[0])
                    xmax = max(p1[0], p2[0])
                    for x in range(xmin, xmax + 1):
                        self.grid[(x,y)] = ROCK
                p1 = p2

    def show(self):
        for l in range(self.ymin, self.ymax +1):
            line = f"{l:4} "
            for c in range(self.xmin, self.xmax +1):
                val = self.grid[(c, l)]
                if val == ROCK:
                    line += '#'
                elif val == SAND:
                    line += "o"
                elif val == AIR:
                    line += "."
                else:
                    line +=  "-"
            ic (line)


    def sand_pour(self, x, y):

        while self.grid[(x, y+1)] == AIR:
            y += 1
            if y > self.ymax:
                raise FallOutException("y max !")
        
        if self.grid[(x-1, y+1)] != AIR:
            if self.grid[(x+1, y+1)] != AIR:
                # blocked
                return x, y
            else:
                if y > self.ymax:
                    raise FallOutException("y max !")
                if x < self.xmin or x > self.xmax:
                    raise FallOutException("x !")

                return self.sand_pour(x+1, y+1)
        else:
            if y > self.ymax:
                raise FallOutException("y max !")
            if x <= self.xmin or x >= self.xmax:
                raise FallOutException("x !")
            # ic ("air on", x-1, y+1)
            return self.sand_pour(x-1, y+1)


    def sand_pour2(self, x, y):
        self.grid[(x, self.ymax)] = ROCK 
        self.grid[(x-1, self.ymax)] = ROCK 
        self.grid[(x+1, self.ymax)] = ROCK 
        while self.grid[(x, y+1)] == AIR:
            y += 1
        
        if self.grid[(x-1, y+1)] != AIR:
            if self.grid[(x+1, y+1)] != AIR:
                if x == 500 and y == 0:
                    raise SandFullException("ok")
                return x, y
            else:
                return self.sand_pour2(x+1, y+1)
        else:
            return self.sand_pour2(x-1, y+1)


def part1(grille: Grid):
    
    i = 0
    while  True:
        try:
            x, y = grille.sand_pour(500, 0)
            grille.grid[(x, y)] = SAND
        except  FallOutException as e:
            print(f"part1 i: {i}", e)
            grille.show()
            break
        i += 1
    return i


def part2(grille: Grid):
    grille.ymax += 2
    # grille.show()
    i = 0
    while  True:
        try:
            x, y = grille.sand_pour2(500, 0)
            grille.grid[(x, y)] = SAND
            # grille.show()
        except  GridException as e:
            print(f"part2 i: {i}", e)
            grille.show()
            break
        i += 1
    return i +1

def main():
    reponse1 = 0
    reponse2 = 0

    file_data = "exemple.txt"
    file_data = "input.txt"

    with open(file_data, 'r') as f:
        lines = [line.strip("\n") for line in f.readlines()]

    # TODO: your code here
    # commun_part
    grille = Grid(lines)
    grille.show()
    ic(grille.xmin, grille.xmax, grille.ymin, grille.ymax)

    grille2 = deepcopy(grille)
    reponse1 = part1(grille)
# 
    reponse2 = part2(grille2)
    
    return reponse1, reponse2


if __name__ == "__main__":
    reponse1, reponse2 = main()

    print(f"reponse part1:{reponse1}")
    print(f"reponse part2:{reponse2}")

    add_reponse("reponse part1", reponse1)
    add_reponse("reponse part2", reponse2)

# -----------------------------
#  1 , 208 too low - 1061
# reponse part1: 1061
# reponse part2: 25055
# reponsepart1: 1061
# reponse part2: 25055