#!/usr/bin/python3

# part1.py

"""
--- Day 4: Giant Squid ---

You're already almost 1.5km (almost a mile) below the surface of the ocean, already so deep that you can't see any sunlight. What you can see, however, is a giant squid that has attached itself to the outside of your submarine.

Maybe it wants to play bingo?

Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random, and the chosen number is marked on all boards on which it appears. (Numbers may not appear on all boards.) If all numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)

The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time. It automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input). For example:

7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7

After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no winners, but the boards are marked as follows (shown here adjacent to each other to save space):

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are still no winners:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

Finally, 24 is drawn:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

At this point, the third board wins because it has at least one complete row or column of marked numbers (in this case, the entire top row is marked: 14 21 17 24 4).

The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on that board; in this case, the sum is 188. Then, multiply that sum by the number that was just called when the board won, 24, to get the final score, 188 * 24 = 4512.

To guarantee victory against the giant squid, figure out which board will win first. What will your final score be if you choose that board?

To begin, get your puzzle input.
"""
import os

global ROOT_DIR
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
import sys

path =  "F:\\Zone Sauvegarde\\Documents\\Documents Marc\\Programmation\\github-MPonchon\\aoc"
sys.path.append(path)

from utils import loader
# from loader import load_data, loader

def read_grilles(lines :list) -> list:
    lines.append("")  # ajout derniere grille
    grilles = {}
    grille = []
    no_grille = 0
    for line in lines:
        if line == "":
            if grille == []:
                continue
            # print("new grille", grille)
            ngrille = []
            for gline in grille:
                temp = gline.split(' ')
                temp = [(int(e), False) for e in temp if e != '' ]
                ngrille.append(temp)
                # ngrille = [int(i) for i in gline[0].split(' ')]
            # print("no_grille", no_grille)
            # print("new grille2 ", ngrille)
            no_grille += 1
            grilles[no_grille] = ngrille
            grille = []
            continue
        grille.append(line)
    return grilles

def read_numbers(lines: list) -> list:
    return [int(i) for i in lines[0].split(',')]


def mark_grilles(grilles, n):
    for no, grille in grilles.items():
        mark_grille(grille, n)


def mark_grille(grille, n) -> None:
    # print("grille:", grille)
    for no_line, line in enumerate(grille):
        # print("line: ", line)
        nline = []
        for tup in line:
            num = tup[0]
            if num == n:
                tup = (n, True)
            nline.append(tup)
        grille[no_line] = nline

def check_win_grilles(grilles) -> bool:
    for no, grille in grilles.items():
        # mark grille
        # print("grille no:", no)
        # print("grille:", grille)
        if check_win_grille(grille):
            return True
    return False

def check_win_grille(grille: list) -> bool:
    for no_line, line in enumerate(grille):
        # check row
        print("line: ", line)
        nb_mark = 0
        for num, mark in line:
            if mark:
                nb_mark += 1
        print("nb_mark: ", nb_mark)
        if nb_mark == 5:
            return True
    return False

def sol(grilles, numbers) -> int:

    marks = set()
    for n in numbers:
        if n in marks:
            continue
        marks.add(n)

        if  check_win_grille(grilles):
            print("yes")

    return 0

if __name__ == "__main__":
    print("AOC: part1")


    # get data
    path_to_file = os.path.join(os.getcwd(), 'data.txt')
    data = loader.load_data(path_to_file)

