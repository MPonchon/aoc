#! /bin/env python3
#
# https://adventofcode.com/
#

from icecream import ic
from copy import deepcopy
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


def move_crates(
    nb_crates: int,
    from_stack: int,
    to_stack: int,
    piles: dict
) -> dict:

    for _ in range(nb_crates):
        crate = piles[from_stack].pop(0)
        piles[to_stack].insert(0, crate)
    return piles


def move_crates_keep_order(
    nb_crates: int,
    from_stack: int,
    to_stack: int,
    piles: dict
) -> dict:

    temp = []

    for _ in range(nb_crates):
        crate = piles[from_stack].pop(0)
        temp.append(crate)

    for _ in range(nb_crates):
        crate = temp.pop()
        piles[to_stack].insert(0, crate)

    return piles


def main():

   # file_data = "exemple.txt"
    file_data = "input.txt"

    piles = defaultdict(lambda: [])
    commands = []

    def index_drawing(index: int) -> float:
        return 1+(index-1)/4

    with open(file_data, 'r') as f:
        for line in f.readlines():
            line = line.strip("\n")
            if line.startswith("move"):
                commands.append(
                    [int(i) for i in line
                        .replace('move', '')
                        .replace('from', '')
                        .replace('to', '')
                        .strip()
                        .split('  ')])
                # ic(commands)
            else:
                [piles[index_drawing(i)].append(c)
                    for i, c in enumerate(line)
                    if ord(c) > 64 and ord(c) < 91]
                # ic(piles)

    piles2 = deepcopy(piles)  # part 2

    for command in commands:
        piles = move_crates(*command, piles)

    message_part1 = ""
    for num in sorted(list(piles.keys())):
        # ic(piles[num][0])
        message_part1 += piles[num][0]

    # part 2
    for command in commands:
        piles2 = move_crates_keep_order(*command, piles2)

    message_part2 = ""
    for num in sorted(list(piles2.keys())):
        # ic(piles2[num][0])
        message_part2 += piles2[num][0]

    return message_part1, message_part2


if __name__ == "__main__":
    reponse1, reponse2 = main()
    print(f"reponse part1:{reponse1}")
    print(f"reponse part2:{reponse2}")
    add_reponse("reponse part1", reponse1)
    add_reponse("reponse part2", reponse2)

# -----------------------------
# reponse part1: BZLVHBWQF
# reponse part2: TDGJQTZSL

# part1: BZLVHBWQF
# part2: TDGJQTZSL
