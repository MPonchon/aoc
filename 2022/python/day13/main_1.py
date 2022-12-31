#! /bin/env python3
#
# https://adventofcode.com/
#

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


def compare_int(pair1, pair2) -> Tuple[bool, int]:
    if pair1 < pair2:
        return True, DONE

    elif pair1 > pair2:
        return False,  DONE

    else:
        return False, NOTDONE


def compare_list(pair1, pair2) -> Tuple[bool, int]:
    # ic("compare_list", pair1, pair2)
    l1, l2 = len(pair1), len(pair2)
    if l1 == 0:
        return True, DONE
    if l2 == 0:
        return False, DONE
    # ic(l1,l2)
    if l1 <= l2:
        for i in range(l1):
            check, finish = compare_iter(pair1[i], pair2[i])
            if finish == DONE:
                return check, finish 
        return True, DONE

    # if l1 == l2:
    #     for i in range(l1):
    #         check, finish = compare_iter(pair1[i], pair2[i])
    #         if finish == DONE:
    #             return check, finish 
    #     return True, NOTDONE

    else:
        # return not compare_list(pair2, pair1) 
        for i in range(l2):
            check, finish = compare_iter(pair1[i], pair2[i])
            if finish == DONE:
                return check, finish 
        return False, DONE


def compare_iter(pair1, pair2) -> Tuple[bool, int]:
    # ic(pair1, pair2)
    check = False
    if isinstance(pair1, int) and isinstance(pair2, int):
        check, finish = compare_int(pair1, pair2)
    
    elif isinstance(pair1, list) and isinstance(pair2, int):
        check, finish  = compare_iter(pair1, [pair2])

    elif isinstance(pair1, int) and isinstance(pair2, list):
        check, finish  = compare_iter([pair1], pair2)
    
    else:   # list vs list
        check, finish = compare_list(pair1, pair2)
    # ic(check, finish)
    return check, finish 


def is_ordered_g(pair1, pair2)-> bool:
    l1, l2 = len(pair1), len(pair2)
    if l1 <= l2:
        for i in range(l1):
            check, finish = compare_iter(pair1[i], pair2[i])
            if finish == DONE:
                return check 
        return True

    else:
        return not is_ordered_g(pair2, pair1)

    # elif l1 == l2:
    #     for i in range(l1):
    #         check, finish = compare_iter(pair1[i], pair2[i])
    #         if finish == DONE:
    #             return check
    #     # ic(pair1)
    #     # ic(pair2)
    #     raise ValueError ("l1==l2 comp en echec")

    # else:
    #     for i in range(l2):
    #         check, finish = compare_iter(pair1[i], pair2[i])
    #         if finish == DONE:
    #             return check 
    #     return False




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

    # ic(pairs)
    somme = 0
    for i, pair in enumerate(pairs):
        # if i != 6:
        #     continue
        # ic(i, pair)
        ordered = is_ordered_g(*pair)
        if ordered:
            # ic(i, pair)
            # ic(i+1, ordered)
            print(f"- pair {i+1}: {ordered}")
            somme += (i+1)
    
    reponse1 = somme
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
# reponse part1: 5923
# reponse part2: 0
