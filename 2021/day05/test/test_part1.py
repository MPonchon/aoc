#!/usr/bin/env python3

# test_part1.py

# python -m unittest test.test_part1
# python3 -m unittest test.test_part1

import unittest

import os
from utils import loader
from part1 import get_thlines, check_coord_x, check_coord_y, point_in_line, compute_points, get_maxi


class TestPart1(unittest.TestCase):

    def setUp(self):
        self.exemple = loader.load_data("exemple.txt")

    # @unittest.skip("reason for skipping")
    def test_exemple(self):
        print("* test_exemple")

    # @unittest.skip("reason for skipping")
    def test_get_thlines(self):
        print("* test_get_thlines")
        
        maliste = get_thlines(self.exemple, True)
        print(maliste)
        self.assertEqual( ((0, 9), (5, 9)), maliste[0])

        print(sorted(maliste))


    @unittest.skip("reason for skipping")
    def test_get_maxi(self):
        print("* test_get_maxi")
        
        maliste = get_thlines(self.exemple, True)

        x, y = get_maxi(maliste)

        self.assertEqual( (9,9), (x,y) )



    @unittest.skip("reason for skipping")
    def test_check_coord_on_x(self):
        print("* test_check_coord_on_x")
        
        self.assertTrue( check_coord_x(0, 1, 0, 0, 0, 2))
        self.assertFalse(check_coord_x(0, 3, 0, 0, 0, 2))
        self.assertFalse(check_coord_x(1, 1, 0, 0, 0, 2))

    @unittest.skip("reason for skipping")
    def test_check_coord_on_y(self):
        print("* test_check_coord_on_y")
        
        self.assertTrue( check_coord_y(0, 1, 0, 1, 5, 1))
        self.assertFalse(check_coord_y(0, 3, 4, 3, 9, 3))
        self.assertFalse(check_coord_y(1, 1, 0, 0, 0, 0))

        self.assertTrue( check_coord_y(0, 9, 0, 9, 5, 9))



    @unittest.skip("reason for skipping")
    def test_point_in_line(self):
        print("* test_point_in_line")
        
        thline = ((0,0), (0, 5))

        for y in range(6):
            self.assertTrue(point_in_line((0, y), thline))
        self.assertFalse(point_in_line((0,6), thline))
        self.assertFalse(point_in_line((1,6), thline))
        self.assertFalse(point_in_line((1,1), thline))

        thline = ((0, 9), (5, 9))
        self.assertTrue(point_in_line((0, 9), thline))

        thline = ((7, 0), (7, 4)) 
        self.assertTrue(point_in_line((7, 4), thline))
        thline = ((0, 9), (2, 9))
        self.assertFalse(point_in_line((7, 4), thline))

        thline = ((9, 4), (3, 4))
        self.assertTrue(point_in_line((3, 4), thline))
        # 3, 4, thline: ((9, 4), (3, 4)) ; inside: False


    @unittest.skip("reason for skipping")
    def test_compute_points(self):
        print("* test_compute_points")

        thlines = get_thlines(self.exemple, True)
        # print(thlines)
        points = compute_points(thlines)

        print(points)
