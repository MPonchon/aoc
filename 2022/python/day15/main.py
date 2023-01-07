#! /bin/env python3
#
# https://adventofcode.com/
#

from collections import defaultdict
from functools import total_ordering
from typing import Set, Tuple
from icecream import ic
from collections import namedtuple
from geometrie_2d import man_dist_pt, point_in_range


def add_reponse(tag, reponse):
    import subprocess
    import os
    path_to_main = os.path.join(os.getcwd(), "main.py")
    if os.path.exists(path_to_main):
        command = f"sed -i 's/# {tag}.*$/# {tag}: {reponse}/g' {path_to_main}"
        subprocess.run(command, shell=True)
    else:
        ic(f"Erreur chemin: {path_to_main}")


# def senors_in_range(xm: int, ym: int, sensors):
#     """
#         liste des sensor a porte a l'ordonnée y
#     """
#     sensors_in_range = []
#     for key in sensors:
#         x,y,d = key

def load_data(lines):
    beacons = defaultdict(lambda : set())  # abcisse des beacons a l'ordonnée
    # sensors = defaultdict(lambda : tuple()) 
    sensors = set()

    for line in lines:
        parts = line.replace(':', '').replace(',', '').strip("\n").split(" ")
        x_sensor = int(parts[2][2:])
        y_sensor = int(parts[3][2:])
        x_beacon = int(parts[8][2:])
        y_beacon = int(parts[9][2:])
        beacons[y_beacon].add(x_beacon)
        # ic(parts)
        distance = man_dist_pt(x_sensor, y_sensor, x_beacon, y_beacon)
        # sensors[(x_sensor, y_sensor, distance)] = (x_beacon, y_beacon)
        sensors.add((x_sensor, y_sensor, distance))
    return sensors, beacons


def part1(lines, ym=10):
    sensors, beacons = load_data(lines)

    abscisses = set()
    for key in sensors:
        xs, ys, dist  = key 
        ic(xs, ys, dist )
        # sensor a portee
        ym_min = ys - dist
        ym_max = ys + dist 
        if ym_min > ym:
            # print(f"sensor trop bas ({xs}, {ys}, {dist})")
            continue
        if ym_max < ym:
            # print(f"sensor trop haut ({xs}, {ys}, {dist})")
            continue

        # test aux limites du sensors 
        # deltay = 0  -> xm - x  = d ->  xm = xs -d ; xm = xs + d
        dist_remaining = dist - abs(ym - ys)
        xm_min = xs - dist_remaining
        xm_max = xs + dist_remaining


        for xm in range(xm_min, xm_max +1):
            if xm not in abscisses:
                if point_in_range(xm, ym, xs, ys, dist):
                    abscisses.add(xm)
                    # ic("abscisses,", abscisses)

    # ic(abscisses)
    # ic(len(abscisses))
    count = 0
    if ym in beacons:
        for xb in beacons[ym]:
            if xb in abscisses:
                count += 1 
    reponse1 = len(abscisses) - count
    return reponse1


def main():
    reponse1 = 0
    reponse2 = 0

    file_data = "exemple.txt" ;ym = 10      ; max_range = 20
    file_data = "input.txt" ;  ym = 2000000; max_range = 4000000

    with open(file_data, 'r') as f:
        lines = [line.strip("\n") for line in f.readlines()]


    # TODO: your code here
    # commun_part
    reponse1 = part1(lines, ym)

    return reponse1, reponse2


if __name__ == "__main__":
    reponse1, reponse2 = main()

    print(f"reponse part1:{reponse1}")
    print(f"reponse part2:{reponse2}")

    add_reponse("reponse part1", reponse1)
    add_reponse("reponse part2", reponse2)

# -----------------------------
# reponse part1: 0
# reponse part2: 0
# memo part1: 5878678
# memo part2: 0
