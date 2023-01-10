#! venv/scripts/python.exe 
# -*- coding: utf-8 -*-

'''
   python3 -m unittest test.test_main
'''

from test.wrappers import print_function_name
import unittest

import sys
import os

from main import *




def test_time():
    # ic(test_time)
    file_data = "exemple.txt"; ym = 10;      max_range = 20
    file_data = "input.txt";   ym = 2000000; max_range = 4000000
    # max_range = 100_000
    # ic(max_range)
    lines = []
    with open(file_data, 'r') as f:
        lines = [line.strip("\n") for line in f.readlines()]

    part2(lines, max_range)
    # ic('fin')

class TestOne(unittest.TestCase):


    @print_function_name
    # @unittest.skip("reason for skipping")
    def test_time_part2(self):
        tps = timeit.Timer(
            'test_time()',
            setup="from test.test_main import test_time")
        ic(tps.repeat(1, 1))
        # ic(tps.timeit())
        # ic| tps.repeat(1, 1): [138.64826103500036]
        # 