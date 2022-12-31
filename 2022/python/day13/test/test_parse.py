#! venv/scripts/python.exe 
# -*- coding: utf-8 -*-

'''
    
   python3 -m unittest test.test_parse


'''

import unittest
import sys


import os

from main import *

class TestParse(unittest.TestCase):

    # @unittest.skip("reason for skipping")
    def test_parse_simple(self):
        chaine = "[ 1, 2 ]"
        self.assertEqual( [1,2],  parse_line(chaine))


    # @unittest.skip("reason for skipping")
    def test_parse_twa_lists(self):
        chaine = "[[1,2], [3,4 ]]"
        self.assertEqual( [[1,2],[3,4]], parse_line(chaine))

    @unittest.skip("reason for skipping")
    def test_parse_two_lists_mid(self):
        chaine = "[[1,2],4, [3,4 ]]"
        self.assertEqual( [[1,2],4,[3,4]], parse_line(chaine))

    # @unittest.skip("reason for skipping")
    def test_parse_one_nested(self):
        chaine = "[ 1, 1, [2,3 ], 4 ]"
        self.assertEqual([1, 1, [2, 3], 4],  parse_line(chaine))


    # @unittest.skip("reason for skipping")
    def test_parse_one_nested_first(self):
        chaine = "[ [2,3 ], 4 ]"
        self.assertEqual([[2, 3], 4],  parse_line(chaine))

    # @unittest.skip("reason for skipping")
    def test_parse_one_nested_last(self):
        chaine = "[ 1, [2,3 ]]"
        self.assertEqual([1, [2, 3]],  parse_line(chaine))

    # @unittest.skip("reason for skipping")
    def test_parse_level3_nested(self):
        chaine = "[ 1, 1, [2, [5,6,7],3 ], 4 ]"
        self.assertEqual( [1, 1, [2, [5, 6, 7], 3], 4],  parse_line(chaine))

    # @unittest.skip("reason for skipping")
    def test_parse_level4_nested(self):
        chaine = "[ 1, 1, [2, [5,6,7]]]"
        self.assertEqual( [1, 1, [2, [5, 6, 7]]],  parse_line(chaine))


    # # @unittest.skip("reason for skipping")
    # def test_parse_two_nested_level3(self):
    #     chaine = '[[1],[2,3,4]]'
    #     self.assertEqual( [[1],[2,3,4]],  parse_line(chaine))