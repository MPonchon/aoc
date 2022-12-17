#! /bin/env python3
#
# https://adventofcode.com/
#

from icecream import ic
from collections import defaultdict

def add_reponse(tag, reponse):
    import subprocess
    import os
    path_to_main = os.path.join(os.getcwd(), "main.py")
    if os.path.exists(path_to_main):
        command = f"sed -i 's/# {tag}.*$/# {tag}: {reponse}/g' {path_to_main}"
        subprocess.run(command, shell=True)
    else:
        ic(f"Erreur chemin: {path_to_main}")


def is_visible(tree_range, start, x):
    step = 1 if start < x else -1
    visible = True
    for i in range(start, x, step):
    # ic(i, line[i], line[x])
        if tree_range[i] >= tree_range[x]:
            visible = False
            break
    return visible


def is_visible_col(lines, start, h, x):
    step = 1 if start < h else -1
    visible = True
    for i in range(start, h, step):
        # ic(i, lines[i][x], line[x])
        if lines[i][x] >= lines[h][x]:
            visible = False
            break
    return visible

def view(tree_range, end, x):
    v = 0
    step = -1 if end < x else 1
    for i in range (x+step, end, step):
        # ic(i, tree_range[i], tree_range[x])
        if tree_range[i] < tree_range[x]:
            v += 1
        else:
            v += 1
            break
    # if v == 0:
    #     v = 1
    return v



def main():
    reponse1 = 0
    reponse2 = 0

    file_data = "exemple.txt"
    file_data = "input.txt"

    with open(file_data, 'r') as f:
        lines = [line.strip("\n") for line in f.readlines()]

    # TODO: your code here
    largeur = len(lines[0])
    hauteur = len(lines)
    count = set()
    max_score = 0
    for h, line in enumerate(lines):
        if h == 0 or h == len(lines) -1:
            continue
        # ic(line)
        for x, tree in enumerate(line):
            if x == 0 or x == len(line) -1:
                continue
            # ic(x, h, tree)
            # left 
            visible = is_visible(line, 0, x)
            if visible:
                count.add((x,h))

            vl = view(line, -1, x)
            # ic(vl)

            # right 
            visible = is_visible(line, len(line)-1, x)
            if visible:
                count.add((x,h))

            vr = view(line, len(line), x)
            # ic(vr)

            # up 
            visible = is_visible_col(lines, 0, h, x)
            if visible:
                count.add((x,h))

            v = 0
            for i in range (h-1, -1, -1):
                # ic(i, lines[i][x], lines[h][x], v)
                if lines[i][x] < lines[h][x]:
                    v += 1
                else:
                    v += 1
                    break
                # ic(i, lines[i][x], lines[h][x], v)
            vu = v
            # return v
            # ic (v)

            # down
            visible = is_visible_col(lines, len(lines) -1, h, x)
            if visible:
                count.add((x,h))

            v = 0
            for i in range (h+1, len(lines)):
                # ic(i, lines[i][x], lines[h][x], v)
                if lines[i][x] < lines[h][x]:
                    v += 1
                else:
                    v += 1
                    break
            #  ic (v)
            vd = v
            score = vl * vr * vu * vd
            max_score = max(max_score, score)

    reponse1 = len(count) + 2*(largeur-1) + 2*(hauteur -1)
    reponse2 = max_score


    return reponse1, reponse2

# def check_visible(line, x , therange, step)

if __name__ == "__main__":
    reponse1, reponse2 = main()
    print(f"reponse part1:{reponse1}")
    print(f"reponse part2:{reponse2}")
    add_reponse("reponse part1", reponse1)
    add_reponse("reponse part2", reponse2)

# -----------------------------
# reponse part1: 1733
# reponse part2: 284648
