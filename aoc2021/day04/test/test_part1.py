#!/usr/bin/python3

# test_part1.py

# python -m unittest test.test_part1

import unittest

import sys
path =  "F:\\Zone Sauvegarde\\Documents\\Documents Marc\\Programmation\\github-MPonchon\\aoc"
sys.path.append(path)

import os
from utils import loader

from part1 import ROOT_DIR, read_grilles, read_numbers, sol, mark_grille, mark_grilles, check_win_grille, check_win_grilles


class TestPart1(unittest.TestCase):


    def setUp(self) -> None:
        self.ptf_exemple = os.path.join(ROOT_DIR, "exemple.txt")
        self.exemple  = loader.load_data(self.ptf_exemple)

    # @unittest.skip("reason for skipping")
    def test_Par_test(self):
        print("* test_Par_test")

    @unittest.skip("reason for skipping")
    def test_read_grilles(self):
        print("* test_read_grilles")

        data = loader.load_data(self.ptf_exemple)
        # print(data)
        grilles = read_grilles(data[1:])
        print("grilles:", grilles)

    @unittest.skip("reason for skipping")
    def test_read_numbers(self):
        print("* test_read_numbers")
        data = read_numbers(self.exemple)
        print("data:", data)


    # @unittest.skip("reason for skipping")
    def test_mark_grille(self):
        print("* test_mark_grilles")
        nums = read_numbers(self.exemple)
        # print("nums:", nums)
        data = loader.load_data(self.ptf_exemple)
        grilles = read_grilles(data[1:])

        grille = grilles[1]
        mark_grille(grille, 22)
        mark_grille(grille, 13)
        print("grille:", grille)
        print("grille:", grilles[1])


    @unittest.skip("reason for skipping")
    def test_mark_grilles(self):
        print("* test_mark_grilles")
        nums = read_numbers(self.exemple)
        # print("nums:", nums)
        data = loader.load_data(self.ptf_exemple)
        grilles = read_grilles(data[1:])
        result = mark_grilles(grilles, 22)
        print("grilles:", grilles)


    @unittest.skip("reason for skipping")
    def test_check_win_grille(self):
        print("* test_check_win_grille")
        # nums = read_numbers(self.exemple)
        # print("nums:", nums)
        data = loader.load_data(self.ptf_exemple)
        grilles = read_grilles(data[1:])
        mark_grilles(grilles, 22)
        result = check_win_grille(grilles[1])
        print("grilles:", grilles[1])


    @unittest.skip("reason for skipping")
    def test_check_win_grilles(self):
        print("* test_check_win_grilles")
        nums = read_numbers(self.exemple)
        # print("nums:", nums)
        data = loader.load_data(self.ptf_exemple)
        grilles = read_grilles(data[1:])
        # print("grilles:", grilles[1])
        # result = check_win_grille(grilles)
        mark_grilles(grilles, 22)
        mark_grilles(grilles, 13)
        mark_grilles(grilles, 17)
        print("grilles:", grilles[1])
        # print("result:", result)
        # mark_grilles(grilles, 13)
        # print("grilles:", grilles[1])
        # print("result:", result)
        # mark_grilles(grilles, 17)
        # mark_grilles(grilles, 11)
        # mark_grilles(grilles, 0)
        # print("grilles:", grilles[1])
        # print("result:", result)

        # # result = sol(grilles, nums)




    @unittest.skip("reason for skipping")
    def test_sol(self):
        print("* test_sol")
        nums = read_numbers(self.exemple)
        # print("nums:", nums)
        data = loader.load_data(self.ptf_exemple)
        grilles = read_grilles(data[1:])
        result = sol(grilles, nums)
