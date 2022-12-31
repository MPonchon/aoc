#! /bin/env python3
#
# https://adventofcode.com/
#

from functools import cmp_to_key
from typing import Tuple
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

DONE = 0
NOTDONE = 1

LESS = -1
EQUAL = 0
MORE = 1


def ordered(pair1: int|list, pair2: int|list)-> int:
    check = 0
    if isinstance(pair1, int) and isinstance(pair2, int):
        if pair1 < pair2:    return -1
        elif pair1 > pair2:  return 1
        else:                return 0

    elif isinstance(pair1, list) and isinstance(pair2, int):
        check  = ordered(pair1, [pair2])

    elif isinstance(pair1, int) and isinstance(pair2, list):
        check  = ordered([pair1], pair2)
    
    else:
        l1, l2 = len(pair1), len(pair2)
        if l1 < l2:
            for i in range(l1):
                check = ordered(pair1[i], pair2[i])
                if check != 0:
                    return check 
            return -1
        
        elif l1 == l2:
            for i in range(l1):
                check = ordered(pair1[i], pair2[i])
                if check != 0:
                    return check 
            return 0

        else: # l1 > l2:
            for i in range(l2):
                check = ordered(pair1[i], pair2[i])
                if check != 0:
                    return check 
            return 1

    return check


def closing(line: str, p1: int)->int:
    lvl = 0
    for i, c in enumerate(line[p1:]):
        if c == "[":
            lvl += 1
        if c== "]":
            lvl -= 1
        if lvl == 0 and c == "]":
            return i + p1
    return -1


def add_part(part: str) -> list:
    thelist = []
    if not part:
        return thelist
    # ic(part, len(part))
    if part[len(part)-1] == ',':
        part = part[0:len(part)-1]
    if part and part[0] == ',':
        part = part[1:]
    
    if part:
        if "," in part:
            thelist.extend(
                [int(i) for i in part.split(",")])
        else:
            thelist.append(int(part))
    return thelist


def parse_line(line: str)-> list:
    if line[0] != "[":
        raise ValueError("debut de chaine # [ !") 
    if line[len(line)-1] != "]":
        raise ValueError("fin de chaine # ] !") 

    line = line.replace(" ", "")

    thelist = []
    if len(line)==2:
        return thelist

    line = line[1:len(line)-1]
    
    if "[" not in line:
        if "," in line:
            return [int(i) for i in line.split(",")]
        else:
            return [int(line)]
    else:    
        # composition de listes
        p = line.find("[", 0)
        part1 = line[:p]
        if part1:
            thelist.extend(add_part(part1))

        while p != -1:
            p2 = closing(line, p)
            temp = line[p:p2+1]
            if temp:
                thelist.append(parse_line(temp))
            p = line.find("[", p2+1)

            if p == -1:
                part2 = line[p2+1:]
            else:
                part2 = line[p2+1:p]

            thelist.extend(add_part(part2))
    return thelist


def main():
    reponse1 = 0
    reponse2 = 0

    file_data = "exemple.txt"
    file_data = "input.txt"
# 
    with open(file_data, 'r') as f:
        lines = [line.strip("\n") for line in f.readlines()]

    # TODO: your code here
    pairs = []
    for i in range(0, len(lines), 3):
        # ic(lines[i])
        p1 = parse_line(lines[i])
        p2 = parse_line(lines[i+1])
        # ic(p)
        pairs.append((p1, p2))

    # part 1
    # somme = 0
    # for i, pair in enumerate(pairs):
    #     # if i != 6:
    #     #     continue
    #     # ic(pair)
    #     # ic(i, *pair)
    #     # is_ordered = ordered(pair[0], pair[1])
    #     is_ordered = ordered( *pair)
    #     if is_ordered == -1:
    #         # ic(i, *pair)
    #         # ic(i+1, is_ordered)
    #         # print(f"- pair {i+1}: {is_ordered}")
    #         # print(f"-   p1: {pair[0]} \n -   {pair[1]}")
    #         somme += (i+1)
    
    # reponse1 = somme

    # part2: sorting:
    ic (pairs)
    mylist= []
    for p1, p2 in pairs:
        mylist.append(p1)
        mylist.append(p2)
    mylist.append([[2]])
    mylist.append([[6]])

    li_sorted = sorted(mylist, key=cmp_to_key(ordered))
    ic(li_sorted)
    i1 = li_sorted.index([[2]]) + 1
    i2 = li_sorted.index([[6]]) + 1
    ic(i1, i2)
    reponse2 = i1 * i2
    return reponse1, reponse2


if __name__ == "__main__":
    # chaine = '[[1],[2,3,4]]'
    # chaine = "[1,2]"
    # chaine = "1,2"
    # chaine = "[[1,2], [3,4 ]]"
    # chaine = "[ 1, 2 ]"
    # chaine = "[ 1, 1, [2,3 ], 4 ]"
    # o = parse_line(chaine)
    # print(o)

    reponse1, reponse2 = main()
    print(f"reponse part1:{reponse1}")
    print(f"reponse part2:{reponse2}")
    add_reponse("reponse part1", reponse1)
    add_reponse("reponse part2", reponse2)

# -----------------------------
# -part1: 5923 5996 your answer is too high.
# reponse part1: 0
# reponse part2: 23504
