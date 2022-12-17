#! /bin/env python3
#
# https://adventofcode.com/
#

from icecream import ic


def add_reponse(tag, reponse):
    import subprocess
    import os
    path_to_main = os.path.join(os.getcwd(), "main.py")
    if os.path.exists(path_to_main):
        command = f"sed -i 's/# {tag}.*$/# {tag}: {reponse}/g' {path_to_main}"
        subprocess.run(command, shell=True)
    else:
        ic(f"Erreur chemin: {path_to_main}")


def part1(lines) -> int:
    # TODO: your code here
    # part 1
    # How many positions does the tail of the rope visit at least once?
    positions = set()
    tail = (0,0)
    head = (0,0)
    for line in lines:
        direc, nb_moves = line.split()
        # ic(direc, nb_moves)
        for _ in range(int(nb_moves)):
            head = move(head, direc)
            tail = move_tail(head, tail)
            positions.add(tail)
        show(head, tail)
    return len(positions)


def part2(lines) -> int:
    rope = [(0, 0) for _ in range(9)]
    head = (0,0)
    positions = set()
    for line in lines:
        direc, nb_moves = line.split()
        for _ in range(int(nb_moves)):
            head = move(head, direc)
            rope = move_rope(head, rope)
            positions.add(rope[8])
    return len(positions)


def main():
    reponse1 = 0
    reponse2 = 0

    file_data = "/home/marc/mesprogs/aoc/2022/python/day09/exemple.txt"
    file_data = "input.txt"
    # file_data = "right4.txt"
    # file_data = "exemple2.txt"

    with open(file_data, 'r') as f:
        lines = [line.strip("\n") for line in f.readlines()]

    # TODO: your code here
    # part 1
    reponse1 = part1(lines) 

    # part 2
    reponse2 = part2(lines)

    return reponse1, reponse2


def move_rope(head, rope):
    rope[0] = move_tail(head, rope[0])
    for n in range(1, 9):
        rope[n] = move_knot(rope[n-1], rope[n])
    return rope


def dist_x(head, tail):
    return abs(head[0]-tail[0])


def dist_y(head, tail):
    return abs(head[1]-tail[1])


def move_knot(head, tail) -> tuple:
    temp = move_tail(head, tail)
    if temp != tail:
        return temp
    
    if dist_x(head, tail) == 2 and dist_y(head, tail) == 2:
        d2 = 'R' if tail[0] < head[0] else 'L'
        temp = move(tail, d2)
        d2 = "U" if tail[1] > head[1] else "D"
        temp = move(temp, d2)
    return temp


def move_tail(head: tuple, tail: tuple) -> tuple:
    # ic(align(head, tail))
    # ic(dist_x(head, tail))
    # ic(dist_y(head, tail))
    # cas proche pas d'action
    if align(head, tail)  and (
        dist_x(head, tail) == 1 or  dist_y(head, tail) == 1):
        return tail

    # ic(align(head, tail))
    # cas aligne et delta = 2 
    if align(head, tail) and dist_x(head, tail) == 2:
        d2 = "L" if tail[0] > head[0] else "R"
        tail = move(tail, d2)

    if align(head, tail) and dist_y(head, tail) == 2:
        d2 = "U" if tail[1] > head[1] else "D"
        tail = move(tail, d2)

    # ic(dist_x(head, tail))
    # cas decalé u/d
    if dist_x(head, tail) == 1 and dist_y(head, tail) == 2:
        d2 = "L" if tail[0] > head[0] else "R"
        tail = move(tail, d2)
        d2 = "U" if tail[1] > head[1] else "D"
        tail = move(tail, d2)

    # cas decalé l/r
    if dist_y(head, tail) == 1 and dist_x(head, tail) == 2:
        d2 = "L" if tail[0] > head[0] else "R"
        tail = move(tail, d2)
        d2 = "U" if tail[1] > head[1] else "D"
        tail = move(tail, d2)

    return tail


def move(item, direc: str):
    dirs = { 'R': (1, 0), 'L': (-1,0), 'U': (0, -1), 'D': (0, 1)}
    return (item[0] + dirs[direc][0], item[1] + dirs[direc][1])


def align(head, tail) -> bool:
    return tail[1] == head[1] or tail[0] == head[0]


def show(head, tail, start=(0,0)):
    hmin = min(head[1], tail[1], start[1])
    hmax = max(head[1], tail[1], start[1])
    xmin =  min(head[0], tail[0], start[0])
    xmax =  max(head[0], tail[0], start[0])

    lines = []
    for h in range(hmax - hmin +1):
        line = "." * (xmax - xmin + 1)
        if h == start[1] - hmin:
            x = start[0] - xmin
            line = line[:x] + "s" + line[x +1:]
        if h == tail[1] - hmin:
            x = tail[0] - xmin 
            line = line[:x] + "T" + line[x +1:] 
        if h == head[1] - hmin:
            x = head[0] - xmin 
            line = line[:x] + "H" + line[x +1:] 
        # ic(line)
        lines.append(line)
    # for line in lines:
    #     ic(line)
    #     # print(line)

def show_rope(head, rope, direc, nb_moves, start=(0,0)):
    ic(direc, nb_moves)
    # ic([knot[1] for knot in rope])
    hmin = min(head[1], *[knot[1] for knot in rope], start[1])
    hmax = max(head[1], *[knot[1] for knot in rope], start[1])
    xmin = min(head[0], *[knot[0] for knot in rope], start[0])
    xmax = max(head[0], *[knot[0] for knot in rope], start[0])

    lines = []
    for h in range(hmax - hmin +1):
        line = "." * (xmax - xmin + 1)
        if h == start[1] - hmin:
            x = start[0] - xmin
            line = line[:x] + "s" + line[x +1:]
        for n, knot in enumerate(rope[::-1]):
        # for n, knot in enumerate(rope):
            # ic(9-n)
            if h == knot[1] - hmin:
                x = knot[0] - xmin 
                line = line[:x] + str(9-n) + line[x +1:] 
        
        if h == head[1] - hmin:
            x = head[0] - xmin 
            line = line[:x] + "H" + line[x +1:] 

        ic(line)
        lines.append(line)

if __name__ == "__main__":
    reponse1, reponse2 = main()
    print(f"reponse part1:{reponse1}")
    print(f"reponse part2:{reponse2}")
    add_reponse("reponse part1", reponse1)
    add_reponse("reponse part2", reponse2)
    

# -----------------------------
# reponse part1: 0
# reponse part2: 2259


# -----------------------------
# memo reponse part1: 0
# memo reponse part2: 730 too low
