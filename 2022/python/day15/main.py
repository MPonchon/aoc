#! /bin/env python3
#
# https://adventofcode.com/
#

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

def man_dist(p1 ,p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def in_range_sensor(ps, p1, dmax=9) -> bool:
    man_d = man_dist(ps , p1 )
    # ic(man_d, dmax)
    return man_d <= dmax


def in_range_dx(xs, x1, dmax=1) -> bool:
    return abs(x1 -xs) <= dmax


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
    for sensor in sorted(sensors_ranged):
        # ic(sensor)
        dmax = sensors[sensor].dmax.x + sensors[sensor].dmax.y # dx + dy
        dmax_x = dmax # - dy
        # sensor limited to dmax
        # ic(sensor.x-dmax_x, sensor.x+dmax_x +1)
        for x in range(sensor.x-dmax_x, sensor.x+dmax_x +1):
            # if sensor == (8,7):
            #     ic(x)
            if x not in line_ym and \
                in_range_sensor(sensor, (x, ym), dmax_x):
                    line_ym[x] = 1
                    # ic ("in", x)

                    # abs(sensor.x x) + abd(sensor.y - ym) <= dmax
                    # abs(sensor.x x) <= dmax - abs( sensor.y - ym) 

                    #         dmax = sensors[sensor].dmax.x + sensors[sensor].dmax.y 
                    #                                         dy = abs(y_b - y_s) 


        n += 1
        ic (n , nb)

    nb_libre = len(line_ym) - len(nb_beacons_on_line)
    # ic(line_ym)
    # ic(nb_beacons_on_line)
    # ic(nb_libre)
    return nb_libre


def main():
    reponse1 = 0
    reponse2 = 0

    file_data = "exemple.txt" ;ym = 10
    file_data = "input.txt" ;     ym = 2000000

    with open(file_data, 'r') as f:
        lines = [line.strip("\n") for line in f.readlines()]


    # TODO: your code here
    # commun_part
    sensors = {}
    
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

    # ic(sensors)
    
    reponse1 = part1(sensors, ym)
    ic(reponse1)
    # reponse2 = part2(lines)
    return reponse1, reponse2


if __name__ == "__main__":
    reponse1, reponse2 = main()

    print(f"reponse part1:{reponse1}")
    print(f"reponse part2:{reponse2}")

    add_reponse("reponse part1", reponse1)
    add_reponse("reponse part2", reponse2)

# -----------------------------
# reponse part1: 5878678
# reponse part2: 0
# memo part1: 5878678
# memo part2: 0
