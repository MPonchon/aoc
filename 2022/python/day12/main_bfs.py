#! /bin/env python3
#
# https://adventofcode.com/
#

from icecream import ic
from collections import defaultdict
import math
from heapq import heappop, heappush, heappushpop, heapify
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


def bfs(graphe, start, goal):
    # queue = [ (start, [start]) ]
    queue = [(0, start)]
    visited = set()
    # i = 0
    while queue:
        # node, path = queue.pop(0)
        nb_nodes_vus, node = queue.pop(0)
        visited.add(node)
        # fout.write(f">{node}< path: {path}\n\n")
        # i += 1
        # if i%1000==0:
        #     ic(i,len(visited))
        # ic(queue)

        for voisin in graphe[node]:
            if voisin in visited:
                continue

            if voisin == goal:
                return nb_nodes_vus + 1

            queue.append( (nb_nodes_vus + 1, voisin) )

    return []



def main(fout=None):
    reponse1 = 0
    reponse2 = 0

    file_data = "exemple.txt"
    # file_data = "input.txt"

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

    # for node in sorted(list(graph.keys())):
    #     ic(node, graph[node])
        # fout.write(f"-{node}:\n")
        # for n in sorted(graph[node]):
        #     fout.write(f"   {n}:\n")
        #     #  {graph[node]}\n")
    ic(graph)
    ic(len(graph))

    # 2 - traverse graph
    # BFS 
    ic(start, goal)
    distance = bfs(graph, start, goal)
    reponse1 = distance
    # print(path, len(path))

    return reponse1, reponse2


if __name__ == "__main__":
    with open(os.getcwd() +"/log_day12.txt", "w+") as fout:
        reponse1, reponse2 = main(fout)
        print(f"reponse part1:{reponse1}")
        print(f"reponse part2:{reponse2}")
        add_reponse("reponse part1", reponse1)
        add_reponse("reponse part2", reponse2)

# -----------------------------
# reponse part1: 31
# reponse part2: 0
