#! /bin/env python3
#
# https://adventofcode.com/
#

from functools import total_ordering
from typing import Set, Tuple
from icecream import ic
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])


def add_reponse(tag, reponse):
    import subprocess
    import os
    path_to_main = os.path.join(os.getcwd(), "main.py")
    if os.path.exists(path_to_main):
        command = f"sed -i 's/# {tag}.*$/# {tag}: {reponse}/g' {path_to_main}"
        subprocess.run(command, shell=True)
    else:
        ic(f"Erreur chemin: {path_to_main}")

"""

               1    1    2    2
     0    5    0    5    0    5
-2 ..........#.................
-1 .........###................
 0 ....S...#####...............
 1 .......#######........S.....
 2 ......#########S............
 3 .....###########SB..........
 4 ....#############...........
 5 ...###############..........
 6 ..#################.........
 7 .#########S#######S#........
 8 ..#################.........
 9 ...###############..........
10 ....B############...........
11 ..S..###########............
12 ......#########.............
13 .......#######..............
14 ........#####.S.......S.....
15 B........###................
16 ..........#SB...............
17 ................S..........B
18 ....S.......................
19 ............................
20 ............S......S........
21 ............................
22 .......................B....


               1    1    2    2
     0    5    0    5    0    5
10 ....B---------4--...........
11 ..S..--------434............
12 ......--------2.............
13 .......------212............
14 ........--4321S12.....S.....
15 B........--43212............
16 ..........-SB32.............
17 .............43.S..........B
18 ....S.........4.............


               1    1    2    2
     0    5    0    5    0    5
 7 .---654321S-----?-S-........
 8 ..-8--54321--------.........
 9 ...98765432-------..........
10 ....B87654345678?...........
11 ..S..98---4-----............
12 ......----5----.............
13 .......---6---..............
14 ........-----.S.......S.....
15 B........---................
16 ..........-SB...............
17 ................S..........B
18 ....S.......................
19 ............................
20 ............S......S........
21 ............................
22 .......................B....



"""


# TSegment = namedtuple('Segment', ['left', 'right'])

class Segment():
    """
    Segment de droite
    """

    def __init__(self, l, r):
        self.left = min(l, r)
        self.right = max(l, r)
        

    def __contains__(self, x):
        if isinstance(x, int):
            return x >= self.left and x <= self.right
        elif isinstance(x, Segment):
            return x.left >= self.left and x.right <= self.right


    def merge(self, other) -> bool:
        """
        Fusionne 2 segment, retourne True si fusion ok, False si echec
        """
        if isinstance(other, Segment):
            if other.left in self or other.right in self:
                self.right = max(other.right, self.right)
                self.left = min(other.left, self.left)
                return True

            return False

        else:
            raise ValueError ("Not implemented yet !")
        
    def __repr__(self) -> str:
        return f"|_{self.left},{self.right}_|"

@total_ordering
class CSensor:
    def __init__(self, coord: Point, beacon: Point) -> None:
        self.point = coord
        self.beacon = beacon

        self.man = man_dist(coord, beacon)

    def in_range(self, other: Point) -> bool:
        dist = man_dist(self.point, other)
        return dist <= self.man

    def detection_at_y(self, ym: int, minx, maxx) -> Set:
        detection = set()
        bornes = self._bornes_at_y(ym)
        if bornes:
            for x in range(bornes[0], bornes[1] + 1):
                if x >= minx and x <= maxx:
                    detection.add(x)
        return detection

    def segment_at_y(self, ym: int, minx, maxx) -> Segment|None:
        seg = None
        bornes = self._bornes_at_y(ym)
        xl = bornes[0]
        if xl < minx:
            xl = minx
        xr = bornes[1]
        if xr > maxx:
            xr = maxx
        # ic(bornes, xl, xr, maxx)
        if bornes:
            seg = Segment(xl, xr)
        return seg


    def _bornes_at_y(self, ym: int) -> Tuple[int, int]|None:
        # ic(man)
        dym = abs(ym - self.point.y)
        # ic(dym)
        if self.man < dym:
            return None
        dxm = self.man - dym
        # ic(dxm)
        return self.point.x - dxm, self.point.x + dxm

    def __eq__(self, other):
        return ((self.point, self.beacon) ==
                (other.point, other.beacon))

    def __lt__(self, other):
        return self.point.x < other.point.x

    def __hash__(self):
        return hash(self.point.x * self.point.y*self.beacon.x *self.beacon.y)

    def __repr__(self) -> str:
        return str(self.point.x) +"," +str(self.point.y) 


def man_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def in_range_sensor(ps, p1, dmax=9) -> bool:
    man_d = man_dist(ps , p1 )
    # ic(man_d, dmax)
    return man_d <= dmax


def in_range_dx(xs, x1, dmax=1) -> bool:
    return abs(x1 -xs) <= dmax


def bornes_range_sensor(ps, bs, ym):
    dx = abs(ps.x - bs.x)
    dy = abs(ps.y - bs.y)
    man = dx + dy
    # ic(man)
    dym = abs(ym - ps.y)
    # ic(dym)
    if man < dym:
        return None
    dxm = man - dym
    # ic(dxm)
    return ps.x - dxm, ps.x + dxm


def part1(sensors, ym):
    # recherche des sensors a y = 10
    # limites de detection
    # dx + dy
    sensors_ranged = set()

    # parcours des sensors potentiellement dans la portée
    # test au limites NS
    # ajout des bornes
    for sensor in sensors:
        # N et S
        rayon = sensors[sensor].dmax.y + sensors[sensor].dmax.x
        if in_range_sensor(sensor, (sensor.x, ym), rayon):
            sensors_ranged.add(sensor)
    ic(sensors_ranged)

    line_ym = {}
    nb_beacons_on_line = set(
        beacon_d.beacon for beacon_d in 
        (sensors[sensor] for sensor in sensors_ranged) 
        if beacon_d.beacon.y == ym)
    # ic(nb_beacons_on_line)

    nb = len(sensors_ranged)
    n = 0
    # for sensor in sorted(sensors_ranged):
    #     # ic(sensor)
    #     dmax = sensors[sensor].dmax.x + sensors[sensor].dmax.y # dx + dy
    #     dmax_x = dmax # - dy
    #     for x in range(sensor.x-dmax_x, sensor.x+dmax_x +1):
    #         if x not in line_ym and \
    #             in_range_sensor(sensor, (x, ym), dmax_x):
    #                 line_ym[x] = 1
    #     n += 1
    #     ic (n , nb)

    for sensor in sorted(sensors_ranged):
        ic(sensor)
        dmax = sensors[sensor].dmax.x + sensors[sensor].dmax.y # dx + dy
        bornes = bornes_range_sensor(sensor, sensors[sensor].beacon, ym)
        if bornes:
            for x in range(bornes[0], bornes[1]+1):
                if x not in line_ym and \
                    in_range_sensor(sensor, (x, ym), dmax):
                        line_ym[x] = 1
        n += 1
        ic (n , nb)

    no_beacon_here = len(line_ym) - len(nb_beacons_on_line)
    # ic(line_ym)
    # ic(nb_beacons_on_line)
    # ic(nb_libre)
    return no_beacon_here


def beacon_here(sensors, ym, max_range):
    sensors_ranged = set()
    for sensor, csensor in sensors.items():
        # rayon = sensors[sensor].dmax.y + sensors[sensor].dmax.x
        # if in_range_sensor(sensor, (sensor.x, ym), rayon):
        #     sensors_ranged.add(sensor)
        if csensor.in_range( Point(sensor.x, ym)):
            sensors_ranged.add(sensor)

    # line_ym = set(i for i in range(max_range))
    line_ym = []
    # ic(line_ym)
    # ic(sensors_ranged)

    for sensor in sorted(sensors_ranged):
        # dmax = sensors[sensor].dmax.x + sensors[sensor].dmax.y # dx + dy
        # bornes = bornes_range_sensor(sensor, sensors[sensor].beacon, ym)
        csensor =  sensors[sensor]
        # s = csensor.detection_at_y(ym, 0, max_range)
        segment = csensor.segment_at_y(ym, 0, max_range)
        if segment:
            # merge segments
            merged = False
            for seg in line_ym:
                merged = seg.merge(segment)
                if merged:
                    break
            if not merged:
                line_ym.append(segment)
    return line_ym


def freq(x):    return 56_000_011 - x * 4_000_000
# 19 × 131 × 149 × 151


def part2(sensors, ym, max_range):
    print("part2")
    ic(ym, max_range)
    beqs = set()
    line_ym = beacon_here(sensors, 11, max_range)

    # for y in range(11, 12):
    for y in range(0, max_range+1):
        line_ym = beacon_here(sensors, y, max_range)
        # ic(y, line_ym)
        for seg in line_ym:
            # ic(seg)
            for x in range(seg.left, seg.right +1):
                yfreq = freq(x)
                if yfreq > max_range or yfreq < 0: continue
                # ic(y, x, yfreq)
                beqs.add ((x, yfreq))
            
        if y%10 == 0:
            ic(y, line_ym, beqs)
    ic(beqs)

    for beq in beqs:
        x ,y = beq
        yfreq = freq(x)
        if int(yfreq) == yfreq:
            ic(beq)
            return beq


def main():
    reponse1 = 0
    reponse2 = 0

    file_data = "exemple.txt" ;ym = 10      ; max_range = 20
    file_data = "input.txt" ;  ym = 2000000; max_range = 4000000

    with open(file_data, 'r') as f:
        lines = [line.strip("\n") for line in f.readlines()]


    # TODO: your code here
    # commun_part
    sensors = {}
    csensors = {}
    
    Sensor = namedtuple('Sensor', ['beacon', 'dmax'])
    for line in lines:
        parts = line.replace(':', '').replace(',', '').strip("\n").split(" ")
        x_s = int(parts[2][2:])
        y_s = int(parts[3][2:])
        x_b = int(parts[8][2:])
        y_b = int(parts[9][2:])
        # ic(parts)
        dx = abs(x_b - x_s)
        dy = abs(y_b - y_s) 
        # r = min(dx, dy)
        sensors[Point(x_s, y_s)] = Sensor(
            beacon = Point(x_b, y_b), 
            dmax = Point(dx, dy))

        csensors[Point(x_s, y_s)] = CSensor(Point(x_b, y_b),Point(dx, dy))

    # ic(sensors)
    
    # reponse1 = part1(sensors, ym)
    # ic(reponse1)

        # m
    # 

    reponse2 = part2(csensors, ym, max_range)
    return reponse1, reponse2


if __name__ == "__main__":
    reponse1, reponse2 = main()

    print(f"reponse part1:{reponse1}")
    print(f"reponse part2:{reponse2}")

    add_reponse("reponse part1", reponse1)
    add_reponse("reponse part2", reponse2)

# -----------------------------
# reponse part1: 0
# reponse part2: (14, 11)
# memo part1: 5878678
# memo part2: 0
