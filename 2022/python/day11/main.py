#! /bin/env python3
#
# https://adventofcode.com/
#

from typing import Tuple
from icecream import ic
import re
from pprint import pprint

def add_reponse(tag, reponse):
    import subprocess
    import os
    path_to_main = os.path.join(os.getcwd(), "main.py")
    if os.path.exists(path_to_main):
        command = f"sed -i 's/# {tag}.*$/# {tag}: {reponse}/g' {path_to_main}"
        subprocess.run(command, shell=True)
    else:
        ic(f"Erreur chemin: {path_to_main}")



class Monkey:



    def __init__(
        self,
        items,
        ope,
        div,
        th_true,
        th_false
    ):
        self.items = items
        self.ope = ope
        self.div = div
        self.th_true = th_true
        self.th_false = th_false
        self.inspect = 0


    def run(self):
        self.inspect += len(self.items)
        ret_list = []
        while self.items:
            wl = self.items.pop(0)
            worry_level = self.operation(wl)
            # ic(worry_level)
            worry_level, id_next_monkey = self.throw_to(worry_level)
            ret_list.append((id_next_monkey, worry_level))
        return ret_list

    def operation(self, value) -> int:
        params = re.split("\+|\*",self.ope)
        params = [s.replace("old", str(value)) for s in params]
        params = [int(s) for s in params]
        # ic (params)
        wl = -1
        if '*' in self.ope:
            wl = params[0] * params[1]
        if '+' in self.ope:
            wl = params[0] + params[1]
        return wl
    

    def throw_to(self, worry_level: int)->int:
        worry_level //= 3
        if worry_level % self.div == 0:
            th_monkey = self.th_true 
        else:
            th_monkey = self.th_false
        return worry_level, th_monkey



    def receive_item(self, item):
        self.items.append(item)


    def __repr__(self) -> str:
        return ",".join([str(i) for i in self.items]) + f" insp {self.inspect}"
        # return f" insp {self.inspect}"

class MonkeyNoDiv(Monkey):
    ppcm = 0

    def throw_to(self, worry_level: int)->int:
        worry_level %= MonkeyNoDiv.ppcm
        if worry_level % self.div == 0:
            # while worry_level  % self.div == 0:
            #     worry_level //= self.div
            # worry_level *= self.div
            # worry_level= int(worry_level)
            th_monkey = self.th_true 
        else:
            th_monkey = self.th_false
        return worry_level, th_monkey

    def __repr__(self) -> str:
        # return ",".join([str(i) for i in self.items]) + f" insp {self.inspect}"
        return f" insp {self.inspect}"



def make_monkey(mk_strings: list, mk_type="DIV") -> Tuple[int, Monkey]:
    id = -1
    for line in mk_strings:
        if "Monkey" in line:  
            id = int( line.split()[1].replace(":",""))
        if "Starting" in line:
            items_list = [int(i) for i in line.split(':')[1].split(",")]
        if "Operation" in line:
            ope = line.split("=")[1]
        if "Test" in line:
            div = int(line.split("by")[1])
        if "If true" in line:
            th_true = int(line.split("monkey")[1])
        if "If false" in line:
            th_false = int(line.split("monkey")[1])

    # ic(id, items_list, ope, div, th_true, th_false)
    if mk_type == "DIV":
        monkey = Monkey(items_list, ope, div, th_true, th_false)
    else:
        monkey = MonkeyNoDiv(items_list, ope, div, th_true, th_false)
    return id, monkey


def main():
    reponse1 = 0
    reponse2 = 0

    file_data = "exemple.txt"
    file_data = "input.txt"

    with open(file_data, 'r') as f:
        # lines = [line.strip("\n") for line in f.readlines()]
        parts = f.read().split("\n\n")

    #  ---------- part 1
    monkeys = {}
    for m in parts:
        id, monkey = make_monkey(m.split("\n"))
        monkeys[id] = monkey

    for round in range(20):
        for id, monkey in monkeys.items():
            ret_list = monkey.run()
            for mk, item in ret_list:
                monkeys[mk].receive_item(item)

    mk_sorted = sorted(monkeys.values(), key=lambda x: x.inspect, reverse=True)
    reponse1 = mk_sorted[0].inspect * mk_sorted[1].inspect

    # ----------- part 2
    ppcm = 1
    monkeys = {}
    for m in parts:
        id, monkey = make_monkey(m.split("\n"), "NODIV")
        monkeys[id] = monkey
        ppcm *= monkey.div
    MonkeyNoDiv.ppcm = ppcm
    ic(MonkeyNoDiv.ppcm)
    for round in range(10000):
        for id, monkey in monkeys.items():
            ret_list = monkey.run()
            for mk, item in ret_list:
                monkeys[mk].receive_item(item)
    ic(monkeys)

    mk_sorted = sorted(monkeys.values(), key=lambda x: x.inspect, reverse=True)
    reponse2 = mk_sorted[0].inspect * mk_sorted[1].inspect

    return reponse1, reponse2


if __name__ == "__main__":
    reponse1, reponse2 = main()
    print(f"reponse part1:{reponse1}")
    print(f"reponse part2:{reponse2}")
    add_reponse("reponse part1", reponse1)
    add_reponse("reponse part2", reponse2)

# -----------------------------
# reponse part1: 90294
# reponse part2: 18170818354

# -----------------------------
# memo reponse part1: 10605, 90294
# memo reponse part2: 18170818354