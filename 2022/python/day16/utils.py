#! /bin/env python3
#

from collections import defaultdict
from typing import List
from icecream import ic
import heapq as heap
import math
from copy import copy


def add_reponse(tag, reponse):
    """
    Ajoute la reponse en fin de fichier main
    remplace le tag par le tag + la reponse
    """
    import subprocess
    import os

    path_to_main = os.path.join(os.getcwd(), "main.py")
    if os.path.exists(path_to_main):
        command = f"sed -i 's/# {tag}.*$/# {tag}: {reponse}/g' {path_to_main}"
        subprocess.run(command, shell=True)
    else:
        print(f"Erreur chemin: {path_to_main}")


def max_pressure(node, remaining_time, opened_valves, graphe, memo):

    if remaining_time <= 1:  # sortie de la reccurence
        return 0  # no more pressure to add !

    pressures = []

    # memoisation:
    key = (node, remaining_time, ",".join(sorted(opened_valves)))
    # ic(key)
    if key in memo:
        return memo[key]
    # ic(node)

    # choice: open valve and get new pressure !
    if node not in opened_valves:
        new_pressure = graphe[node]["rate"] * (remaining_time - 1)
        # ic(node, remaining_time, graphe[node]['rate'], new_pressure)
        current_pressure = new_pressure + max_pressure(
            node, remaining_time - 1, opened_valves | {node}, graphe, memo
        )
        pressures.append(current_pressure)

    # choice: go to node voisin
    for voisin in graphe[node]["voisins"]:
        pressure_voisin = max_pressure(
            voisin, remaining_time - 1, opened_valves, graphe, memo
        )
        pressures.append(pressure_voisin)
    maxi_pressure = max(pressures)

    memo[key] = maxi_pressure  #  memoisation
    # ic(maxi_pressure)
    return maxi_pressure


"""
on cherche a passer par toutes les vannes fermées et les ouvrir
et pas a passer par tous les voisins

a l'etape n:
    je teste toutes les vannes restantes 
        pour une vanne je calcule la pression 
    et j'ajoute le resultat dans une liste

"""


def max_pressure2(
    node,
    remain_valves,
    remaining_time,
    actual_pressure,

    graphe,
    memo,
    dist,
    prof
) -> int:
    """
    Calcul pression
    """
    # ic(node, remaining_time, remain_valves,actual_pressure)

    if remaining_time < 1:
        return actual_pressure
    
    # pressure = actual_pressure
    # pressure += remaining_time * graphe[node]["rate"]

    remain_valves -= {node}     # je teste toutes les vannes restantes
    
    pressions = []
    # ic(remain_valves)
    rm = copy(remain_valves)
    for valve in rm:

        # ic(remain_valves)
        if dist[node][valve] == math.inf:
            continue
        
        if remaining_time < 2: # move + open
            return actual_pressure

        # ouverture et deplacement vers la vanne
        temps = remaining_time - dist[node][valve] - 1

        # calcul pression liberée 
        pressure = actual_pressure
        pressure += temps * graphe[valve]["rate"]
        pressure = max_pressure2(
            valve,
            remain_valves,
            temps,
            pressure,

            graphe,
            memo,
            dist,
            prof +1)

        if prof >= 3:
            ic(prof , valve,remaining_time, actual_pressure, temps)

        pressions.append(pressure)

    if prof == 3:
        ic(prof , node, pressions)
    if pressions:
        best = max(pressions)
    else:
        best = 0
    actual_pressure += best
    return actual_pressure



def max_pressure_both(node1, node2, remaining_time, opened_valves, graphe, memo):

    if remaining_time <= 1:  # sortie de la reccurence
        return 0  # no more pressure to add !

    # ic(node1, node2, remaining_time, opened_valves)

    # memoisation:
    key = (node1, node2, remaining_time, ",".join(sorted(opened_valves)))
    # ic(key)
    if key in memo:
        return memo[key]

    # liste des possibilités au node n
    choices = set()
    choices_n1 = {v for v in graphe[node1]["voisins"]}
    if node1 not in opened_valves:
        choices_n1.add("open" + node1)
    # ic(choices_n1)
    choices_n2 = {v for v in graphe[node2]["voisins"]}
    if node2 not in opened_valves:
        choices_n2.add("open" + node2)
    # ic(choices_n2)

    # deplacements
    for c1 in choices_n1:
        for c2 in choices_n2:
            if c1 == c2:
                continue
            choices.add((c1, c2))

    if not choices:
        return max_pressure_both(
            node1, node2, remaining_time - 1, opened_valves, graphe, memo
        )

    ic(choices)
    pressures = []
    for choice in choices:
        c1, c2 = choice
        # ic(c1, c2)
        new_pressure = 0
        new_valves = set()
        if c1.startswith("open"):
            n1 = c1[4:6]
            new_pressure = graphe[n1]["rate"] * (remaining_time - 1)
            new_valves.add(n1)

            if c2.startswith("open"):
                n2 = c2[4:6]
                new_valves.add(n2)
                new_pressure += graphe[n2]["rate"] * (remaining_time - 1)

            else:
                n2 = c2
        else:
            n1 = c1
            if c2.startswith("open"):
                n2 = c2[4:6]
                new_valves.add(n2)
                new_pressure = graphe[n2]["rate"] * (remaining_time - 1)
            else:
                n2 = c2

        current_pressure = new_pressure + max_pressure_both(
            n1, n2, remaining_time - 1, opened_valves | new_valves, graphe, memo
        )
        pressures.append(current_pressure)

    maxi_pressure = max(pressures)
    ic(maxi_pressure)
    memo[key] = maxi_pressure  #  memoisation
    # ic(maxi_pressure)
    return maxi_pressure


def all_shortest_path(graphe):
    # https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
    dist = {}
    sommets = [v for v in graphe]
    # initialisation avec les dist: 1 min d'un node a l'autre
    for u in (v for v in graphe):
        dist[u] = {}
        # ic(dist)
        for v in (v for v in graphe):
            if v in dist[u]:
                continue
            if v in graphe[u]["voisins"]:
                dist[u][v] = 1
            else:
                dist[u][v] = math.inf

    for v in graphe:
        dist[v][v] = 0

    nb_vertex = len(sommets)
    for k in range(1, nb_vertex):
        for i in range(1, nb_vertex):
            for j in range(1, nb_vertex):
                vi = sommets[i]
                vj = sommets[j]
                vk = sommets[k]
                if dist[vi][vj] > dist[vi][vk] + dist[vk][vj]:
                    dist[vi][vj] = dist[vi][vk] + dist[vk][vj]
    return dist


def show_map(distances):
    # for v in sorted(distances.keys()):
    title = "x  |" + "|".join([f"{v:3}" for v in sorted(distances.keys())])
    print(title)
    for u in sorted(distances.keys()):
        # for v in sorted(distances.keys()):
        # ic(u, v, distances[u][v])
        s = (
            str(u)
            + " |"
            + "|".join([f"{distances[u][v]:3}" for v in sorted(distances.keys())])
        )
        print(s)
