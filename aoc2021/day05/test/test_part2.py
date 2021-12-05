#!/usr/bin/env python3

# test_part2.py

# python -m unittest test.test_part1
# python3 -m unittest test.test_part1

import unittest

import os
from utils import loader
from part1 import get_thlines, check_coord_x, check_coord_y, point_in_line, compute_points, get_maxi
from part2 import *

class TestPart2(unittest.TestCase):

    def setUp(self):
        self.exemple = loader.load_data("exemple.txt")

    # @unittest.skip("reason for skipping")
    def test_exemple(self):
        print("* test_exemple")

    # @unittest.skip("reason for skipping")
    def test_check_coord_diag(self):
        print("* test_check_coord_diag")
        """
        An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.

             0123456789
            0 
            1 L
            2  L
            3   L
            4
            5
        """
    
        self.assertTrue(check_coord_diag(1, 1, 1,1, 3,3))
        self.assertTrue(check_coord_diag(2, 2, 1,1, 3,3))
        self.assertTrue(check_coord_diag(3, 3, 1,1, 3,3))
        self.assertFalse(check_coord_diag(3, 4, 1,1, 3,3))
        self.assertFalse(check_coord_diag(4, 4, 1,1, 3,3))
        self.assertFalse(check_coord_diag(1, 2, 1,1, 3,3))

        """
        An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.

             0123456789
            0 
            1 
            2  
            3   
            4
            5
            6 
            7         L
            8        L
            9       L
             0123456789
        """
    
        self.assertFalse(check_coord_diag(1, 1, 9,7, 7,9))
        self.assertTrue(check_coord_diag(7, 9, 9,7, 7,9))
        self.assertTrue(check_coord_diag(8, 8, 9,7, 7,9))
        self.assertTrue(check_coord_diag(9, 7, 9,7, 7,9))



        self.assertTrue(check_coord_diag(7, 0, 7,0, 7, 4))