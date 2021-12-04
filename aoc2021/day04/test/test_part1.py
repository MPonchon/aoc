#!/usr/bin/python3

# test_part1.py

# python -m unittest test.test_part1

import unittest

import sys
path =  "F:\\Zone Sauvegarde\\Documents\\Documents Marc\\Programmation\\github-MPonchon\\aoc"
sys.path.append(path)

import os
from utils import loader

from part1 import ROOT_DIR, read_grilles, read_numbers, sol, check_win_grille, check_win_grilles, transpose


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


    @unittest.skip("reason for skipping")
    def test_check_win_grille_row(self):
        print("* test_check_win_grille_row")
        # nums = read_numbers(self.exemple)
        # print("nums:", nums)
        data = loader.load_data(self.ptf_exemple)
        grilles = read_grilles(data[1:])
        grille = grilles[1]
        marks = set()
        marks.add(22)
        marks.add(13)
        marks.add(17)
        marks.add(11)
        self.assertFalse(check_win_grille(grille, marks))
        marks.add(0)
        self.assertTrue(check_win_grille(grille, marks))
        

    @unittest.skip("reason for skipping")
    def test_check_win_grilles(self):
        print("* test_check_win_grilles")
        nums = read_numbers(self.exemple)
        # print("nums:", nums)
        data = loader.load_data(self.ptf_exemple)
        grilles = read_grilles(data[1:])
        # print("grilles:", grilles[1])
        # result = check_win_grille(grilles)

        print("grilles:", grilles[1])


    @unittest.skip("reason for skipping")
    def test_sol(self):
        print("* test_sol")
        nums = read_numbers(self.exemple)
        # print("nums:", nums)
        data = loader.load_data(self.ptf_exemple)
        grilles = read_grilles(data[1:])
        result = sol(grilles, nums)


    @unittest.skip("reason for skipping")
    def test_transpose(self):
        print("* test_transpose")

        grille = [
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i']
        ]
        # tgrille = transpose(grille)
        # print("tgrille:", tgrille)
        self.assertEqual(
            [['a', 'd', 'g'], ['b', 'e', 'h'], ['c', 'f', 'i']],
            transpose(grille)
            )

