#! /bin/env python3
#
# https://adventofcode.com/
#

from icecream import ic
from collections import defaultdict
import math
# from heapq import heappop, heappush, heappushpop, heapify
import heapq as heap
import os

def add_reponse(tag, reponse):
    import subprocess
    import os
    path_to_main = os.path.join(os.getcwd(), "main.py")
    if os.path.exists(path_to_main):
        command = f"sed -i 's/# {tag}.*$/# {tag}: {reponse}/g' {path_to_main}"
        subprocess.run(command, shell=True)
    else:
        ic(f"Erreur chemin: {path_to_main}")


def get_voisins(x, y, largeur, hauteur, lines):
    left  = (x - 1, y) if x > 0 else None 
    right = (x + 1, y) if x < largeur -1 else None 
    up = (x, y - 1) if y > 0 else None 
    down = (x, y+1) if y < hauteur -1 else None 
    return [x for x in [left, right, up, down] if x is not None]


def dijkstra(graph, start, goal):
    visited = set()
    pq = []
    map_costs = defaultdict(lambda: float('inf'))
    map_costs[start] = 0
    heap.heappush(pq, (0, start))

    while pq:
        p , node = heap.heappop(pq)
        # ic(p, node)
        visited.add(node)

        if node == goal:
            return  map_costs[goal]

        for voisin in graph[node]:
            if voisin not in visited:
                new_map_costs = map_costs[node] + 1

                if  new_map_costs < map_costs[voisin]:
                    map_costs[voisin] = new_map_costs
                    heap.heappush(pq, (new_map_costs, voisin))
    # raise ValueError("not found")
    return -1





def main(fout=None):
    reponse1 = 0
    reponse2 = 0

    file_data = "exemple.txt"
    file_data = "input.txt"

    with open(file_data, 'r') as f:
        lines = [line.strip("\n") for line in f.readlines()]

    # TODO: your code here
    
    # 1 - make graph from data
    haut = { chr(i+97):i for i in range(26) }
    haut["S"] = haut["a"]
    haut["E"] = haut["z"]

    # ic(haut)

    graph =  defaultdict(lambda : set())#  coord node: [links]
    largeur = len(lines[0])
    hauteur = len(lines)

    ic(largeur, hauteur)
    for y, line in enumerate(lines):
        for x, s in enumerate(line):
            if s == "S":
                start = (y, x)
            elif s == "E":
                goal = (y, x)

            h = haut[s]
            # ic (s, h, x,  y)
            for v in get_voisins(x, y, largeur, hauteur, lines):
                vx, vy = v
                # ic(vx, vy)
                v_str = lines[vy][vx]
                v_value = haut[v_str]

                if v_value  <= h + 1:
                    # graph[(x,y)].add( (vx, vy))
                    graph[(y, x)].add( (vy, vx))

    ic("created graphe:", len(graph))

    # ic(graph)
    # ic(len(graph))

    # 2 - traverse graph
    # ic(start, goal)
    # distance = dijkstra(graph, start, goal)
    # reponse1 = distance

    # -- part 2
    # find list of starts
    starts = []
    for y, line in enumerate(lines):
        for x, s in enumerate(line):
            if s == 'a':
                starts.append((y,x))
    ic(len(starts))
    distances =[]
    for s in starts:
        # ic(s, goal)
        d = dijkstra(graph, s, goal)
        if d != -1:
            distances.append(d)
    ic(distances)
    ic(sorted(distances))
    reponse2 = sorted(distances)[0]
    ic(reponse2)
    return reponse1, reponse2


if __name__ == "__main__":
    with open(os.getcwd() +"/log_day12.txt", "w+") as fout:
        reponse1, reponse2 = main(fout)
        print(f"reponse part1:{reponse1}")
        print(f"reponse part2:{reponse2}")
        add_reponse("reponse part1", reponse1)
        add_reponse("reponse part2", reponse2)

# -----------------------------
# reponse part1: 0
# reponse part2: 439

# memo reponse part1: 440
# memo reponse part2: 439