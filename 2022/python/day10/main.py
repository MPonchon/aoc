#! /bin/env python3
#
# https://adventofcode.com/
#

from icecream import ic


def add_reponse(tag, reponse):
    import subprocess
    import os
    path_to_main = os.path.join(os.getcwd(), "main.py")
    if os.path.exists(path_to_main):
        command = f"sed -i 's/# {tag}.*$/# {tag}: {reponse}/g' {path_to_main}"
        subprocess.run(command, shell=True)
    else:
        ic(f"Erreur chemin: {path_to_main}")


def part1(lines):
    register = 1
    cycle = 0
    x = 0
    cycle_list = [20, 60, 100, 140, 180, 220]
    signals = { x:0 for x  in cycle_list}
    somme = 0
    for i, line in enumerate(lines):
        if 'noop' in line:
            instr = 'noop'
            cycle += 1
            if cycle in signals:    # pair
                strength = cycle * register
                signals[cycle] = strength
                somme += strength
            
        else:
            instr, x = line.split()
            cycle +=1
            if cycle in signals:    # pair
                strength = cycle * register
                signals[cycle] = strength
                somme += strength
            
            cycle += 1
            if cycle in signals:    # pair
                strength = cycle * register
                signals[cycle] = strength
                somme += strength

            register += int(x)
    ic(signals)
    return somme


class Screen:
    BLANK_CHAR = " "

    def __init__(self) -> None:
        self.width = 40
        self.hight = 6
        self.lines = [Screen.BLANK_CHAR * self.width] * 6


    def put_pixel(self, pos: int, pixel=' '):
        if pixel == '.': 
            pixel = Screen.BLANK_CHAR
        no_line = pos // self.width 
        x = pos % self.width 
        self.lines[no_line] = self.lines[no_line][:x] + pixel + self.lines[no_line][x+1:]


    def refresh(self, cycle: int, sprite_line: str):
        pos = cycle % self.width  - 1
        self.put_pixel(cycle -1, sprite_line[pos])

    def display(self):
        print(f"output:")
        for line in self.lines:
            ic(line)



def part2(lines):
    screen = Screen()
    cycle = 0
    x = 0
    register = 1
    BLANK_CHAR = ' '
    sprite_line = "###" + BLANK_CHAR * 37
    for i, line in enumerate(lines):
        if 'noop' in line:
            instr = 'noop'
            cycle += 1
            screen.refresh(cycle, sprite_line)

        else:
            instr, sx = line.split()
            x = int(sx)
            cycle +=1
            screen.refresh(cycle, sprite_line)

            cycle += 1
            screen.refresh(cycle, sprite_line)

            register += x
            sprite_line = BLANK_CHAR * (register-1) + "###" + BLANK_CHAR * (40 - register-2)


    screen.display()
    return "ZGCJZJFL"

def main():
    reponse1 = 0
    reponse2 = 0

    file_data = "exemple.txt"
    file_data = "input.txt"

    with open(file_data, 'r') as f:
        lines = [line.strip("\n") for line in f.readlines()]

    # TODO: your code here

    reponse1 = part1(lines)
    reponse2 = part2(lines)

    return reponse1, reponse2


if __name__ == "__main__":
    reponse1, reponse2 = main()
    print(f"reponse part1:{reponse1}")
    print(f"reponse part2:{reponse2}")
    add_reponse("reponse part1", reponse1)
    add_reponse("reponse part2", reponse2)

# -----------------------------
# reponse part1: 14040
# reponse part2: ZGCJZJFL

# -----------------------------
# memo reponse part1: 14040
# memo reponse part2: ZGCJZJFL
