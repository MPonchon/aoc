#! /bin/env python3
#
# https://adventofcode.com/
#

from collections import defaultdict
from functools import total_ordering
from typing import Set, Tuple
from icecream import ic
from collections import namedtuple
from utils import man_dist_pt, point_in_range, x_in_segment, merge_segments, invert_segments
# from timeit import timeit
import timeit


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


def part1_with_set(lines, ym=10):
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


def search_abscisses(sensors, ym, max_range=None):
    abscisses = []
    for key in sensors:
        xs, ys, dist  = key 
        # ic(xs, ys, dist )
        # sensor a portee
        ym_min = ys - dist
        ym_max = ys + dist 
        if ym_min > ym:
            # print(f"sensor trop bas ({xs}, {ys}, {dist})")
            continue
        if ym_max < ym:
            # print(f"sensor trop haut ({xs}, {ys}, {dist})")
            continue

        # ic(xs, ys, dist )
        # test aux limites du sensors 
        # deltay = 0  -> xm - x  = d ->  xm = xs -d ; xm = xs + d
        dist_remaining = dist - abs(ym - ys)
        xm_min = xs - dist_remaining
        xm_max = xs + dist_remaining
        if max_range is not None:
            if xm_min < 0:
                xm_min = 0
            if xm_max > max_range:
                xm_max = max_range

        # xm in a range ?
        inside = False
        for segment in abscisses:
            if x_in_segment(xm_min, segment) and x_in_segment(xm_max, segment):
                inside = True
                break
            elif x_in_segment(xm_min, segment):
                xm_min = segment[1]
                break
            elif x_in_segment(xm_max, segment):
                xm_max = segment[0]
                break
        
        if inside:
            continue

        # ic(abscisses)
        abscisses.append((xm_min, xm_max))

        abscisses = merge_segments(abscisses)
        # ic("abscisses,", abscisses)
    return abscisses



def part1(lines, ym=10):
    sensors, beacons = load_data(lines)

    abscisses = search_abscisses(sensors, ym)
    # calcul taille
    taille = 0
    for seg in abscisses:
        taille += seg[1] - seg[0]

    # ic(abscisses)
    # ic(len(abscisses))
    count = 0
    if ym in beacons:
        for xb in beacons[ym]:
            if xb in abscisses:
                count += 1 
    reponse1 = taille - count
    return reponse1


def part2(lines, max_range):
    reponse2 = 0
    sensors, _ = load_data(lines)

    for y_b in range(0, max_range):
    # for y_b in range(3_041_245, max_range):
        abscisses = search_abscisses(sensors, y_b, max_range)
        # if y_b%200_000==0:   print(y_b)
        if len(abscisses) == 1:
            continue
        # ic(y_b, abscisses)
        # abscisses = search_abscisses(sensors, 11, max_range)
        # ic(abscisses)
        inv = invert_segments(abscisses)
        # ic(inv)
        # print(f"inv: {inv}")
        if len(inv) == 1:
            tup = inv[0]
            reponse2 = 4_000_000 * tup[0] + y_b
            break
        # ic(inv)
    return reponse2
    """
    ic| y_b: 3041245, abscisses: [(0, 2949121), (2949123, 4000000)]
    ic| inv: [(2949122, 2949122)]

    11796491041245

    """



def main():
    reponse1 = 0
    reponse2 = 0

    file_data = "exemple.txt"; ym = 10      ; max_range = 20
    # file_data = "input.txt" ;  ym = 2000000; max_range = 4000000

    with open(file_data, 'r') as f:
        lines = [line.strip("\n") for line in f.readlines()]


    # TODO: your code here
    # commun_part
    reponse1 = part1(lines, ym)
    reponse2 = part2(lines, max_range)
    return reponse1, reponse2


if __name__ == "__main__":


    
    reponse1 = reponse2 = 0
    # reponse1, reponse2 = main()
    print(f"reponse part1:{reponse1}")
    print(f"reponse part2:{reponse2}")

    add_reponse("reponse part1", reponse1)
    add_reponse("reponse part2", reponse2)

# -----------------------------
# reponse part1: 0
# reponse part2: 0
# memo part1: 5878678
# memo part2: 11796491041245
