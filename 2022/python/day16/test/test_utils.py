#! venv/scripts/python.exe 
# -*- coding: utf-8 -*-

'''
   python3 -m unittest test.test_utils
'''
from test.wrappers import print_function_name
import unittest

import sys
import os


from utils import *


class TestUtils(unittest.TestCase):


    @print_function_name
    @unittest.skip("reason for skipping")
    def test_casewherefunctiondosomething(self):
        # self.assertEqual(expected, functiondosomething())
        graphe = {
        'AA': {'rate': 0, 'voisins': {'II', 'BB', 'DD'}},
            'BB': {'rate': 13, 'voisins': {'CC', 'AA'}},
            'CC': {'rate': 2, 'voisins': {'BB', 'DD'}},
            'DD': {'rate': 20, 'voisins': {'CC', 'AA', 'EE'}},
            'EE': {'rate': 3, 'voisins': {'FF', 'DD'}},
            'FF': {'rate': 0, 'voisins': {'GG', 'EE'}},
            'GG': {'rate': 0, 'voisins': {'FF', 'HH'}},
            'HH': {'rate': 22, 'voisins': {'GG'}},
            'II': {'rate': 0, 'voisins': {'AA', 'JJ'}},
            'JJ': {'rate': 21, 'voisins': {'II'}}}
        parcours(graphe, 'AA')


    @print_function_name
    @unittest.skip("reason for skipping")
    def test_pressure(self):
        # self.assertEqual(expected, functiondosomething())
        graphe = {
        'AA': {'rate': 0, 'voisins': {'II', 'BB', 'DD'}},
            'BB': {'rate': 13, 'voisins': {'CC', 'AA'}},
            'CC': {'rate': 2, 'voisins': {'BB', 'DD'}},
            'DD': {'rate': 20, 'voisins': {'CC', 'AA', 'EE'}},
            'EE': {'rate': 3, 'voisins': {'FF', 'DD'}},
            'FF': {'rate': 0, 'voisins': {'GG', 'EE'}},
            'GG': {'rate': 0, 'voisins': {'FF', 'HH'}},
            'HH': {'rate': 22, 'voisins': {'GG'}},
            'II': {'rate': 0, 'voisins': {'AA', 'JJ'}},
            'JJ': {'rate': 21, 'voisins': {'II'}}}

        opened_valves = {valve for valve in graphe if graphe[valve]["rate"]==0}
        # opened_valves =set()
        ic(opened_valves)
        p = max_pressure('AA', 30, opened_valves, graphe, {})
        ic(p)

    @print_function_name
    # @unittest.skip("reason for skipping")
    def test_pressure2(self):
        # self.assertEqual(expected, functiondosomething())
        graphe = {
        'AA': {'rate': 0, 'voisins': {'II', 'BB', 'DD'}},
            'BB': {'rate': 13, 'voisins': {'CC', 'AA'}},
            'CC': {'rate': 2, 'voisins': {'BB', 'DD'}},
            'DD': {'rate': 20, 'voisins': {'CC', 'AA', 'EE'}},
            'EE': {'rate': 3, 'voisins': {'FF', 'DD'}},
            'FF': {'rate': 0, 'voisins': {'GG', 'EE'}},
            'GG': {'rate': 0, 'voisins': {'FF', 'HH'}},
            'HH': {'rate': 22, 'voisins': {'GG'}},
            'II': {'rate': 0, 'voisins': {'AA', 'JJ'}},
            'JJ': {'rate': 21, 'voisins': {'II'}}}

        opened_valves = { valve for valve in graphe if graphe[valve]["rate"]==0 }
        # opened_valves =set()
        ic(opened_valves)
        p =  max_pressure_both('AA', 'AA', 26, opened_valves, graphe, {})
        ic(p)