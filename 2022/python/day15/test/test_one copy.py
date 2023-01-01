#! venv/scripts/python.exe 
# -*- coding: utf-8 -*-

'''
    
   python3 -m unittest test.test_one


'''

import unittest
import sys
import os

from main import *

def print_function_name(function):
    def new_function(*args, **kwargs):
        if '.' in __name__:
            modname = f"{__name__}".split('.')[1]
        else:
            modname = f"{__name__}"
        print(f'{modname}/{function.__name__}')
        
        ret = function(*args, **kwargs)
        return ret
    return new_function


class TestOne(unittest.TestCase):


    @print_function_name
    @unittest.skip("reason for skipping")
    def test_man_dist(self):
        p1 = (8, 7)
        p2 = (8, 16)
        self.assertEqual(9, man_dist(p1, p2))


    @print_function_name
    @unittest.skip("reason for skipping")
    def test_in_range_sensor(self):
        p1 = (8, 7)
        self.assertTrue(in_range_sensor(p1, (8, 16) ))
        self.assertFalse(in_range_sensor(p1, (8, 17)))


    @print_function_name
    @unittest.skip("reason for skipping")
    def test_in_range_sensor_14(self):
        p1 = (12, 14)
        self.assertTrue(in_range_sensor(p1, (12, 10), 4))
        self.assertFalse(in_range_sensor(p1, (11, 10), 4))


    @print_function_name
    @unittest.skip("reason for skipping")
    def test_bornes_range_sensor(self):
        p1 = Point(4, 4)
        b1 = Point(5, 3)
        # self.assertEqual(None, bornes_range_sensor(p1, b1, 1))

        # self.assertEqual( (4, 4), bornes_range_sensor(p1, b1, 2))
        # self.assertEqual( (3, 5), bornes_range_sensor(p1, b1, 3))
        self.assertEqual( (2, 6), bornes_range_sensor(p1, b1, 4))
        self.assertEqual( (3, 5), bornes_range_sensor(p1, b1, 5))
        self.assertEqual( (4, 4), bornes_range_sensor(p1, b1, 6))
        self.assertEqual(None, bornes_range_sensor(p1, b1, 7))

    @print_function_name
    # @unittest.skip("reason for skipping")
    def test_possible_freq(self):
        # 19 × 131 × 149 × 151
        m = 4_000_000
        for x in range(0, m):
            for y in range(0,m):
                f = freq(x)
                if int(f) == y:
                    ic(x,y, f)
            if x%100==0: 
                pc =100*x/4_000_000
                ic (x, pc)