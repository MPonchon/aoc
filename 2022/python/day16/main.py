#! /bin/env python3
#
# https://adventofcode.com/
#
from utils import add_reponse, max_pressure, max_pressure_both
from icecream import ic


def parse_lines(path_to_file_data):

    with open(path_to_file_data, "r") as f:
        lines = [line.strip("\n") for line in f.readlines()]

    graphe = {}
    for line in lines:
        parts = line.split(" ")
        valve = parts[1]
        rate = int(parts[4].split("=")[1].replace(";", ""))

        graphe[valve] = {
            "rate": rate,
            "voisins": {voisin.replace(",", "") for voisin in parts[9:]},
        }
    return graphe


def part1(graphe):
    opened_valves = {valve for valve in graphe if graphe[valve]["rate"] == 0}
    # opened_valves =set()
    ic(opened_valves)
    p = max_pressure("AA", 30, opened_valves, graphe, {})
    return p


def part2(graphe):
    opened_valves = {valve for valve in graphe if graphe[valve]["rate"] == 0}
    # opened_valves =set()
    ic(opened_valves)
    p = max_pressure_both("AA", "AA", 26, opened_valves, graphe, {})
    return p


def main():
    reponse1 = 0
    # reponse2 = 0

    # file_data = "exemple.txt"
    file_data = "input.txt"

    # TODO: your code here
    graphe = parse_lines(file_data)

    ic(graphe)
    # reponse1 = part1(graphe)

    reponse2 = part2(graphe)
    return reponse1, reponse2


if __name__ == "__main__":
    reponse1, reponse2 = main()

    print(f"reponse part1:{reponse1}")
    print(f"reponse part2:{reponse2}")

    add_reponse("reponse part1", reponse1)
    add_reponse("reponse part2", reponse2)

# -----------------------------
# reponse part1: 0
# reponse part2: 1707
#
# reponse memo part1: 1673
# reponse memo part2: 288788976
#   584056832
