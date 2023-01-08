#! venv/scripts/python.exe 
# -*- coding: utf-8 -*-

'''
    
   python3 -m unittest test.test_seg


'''

import unittest
import sys
import os

from utils import *

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

class TestSeg(unittest.TestCase):


    @print_function_name
    @unittest.skip("reason for skipping")
    def test_merge_segments_simple(self):
        s = [ (0, 3), (3,5)]
        self.assertEqual( [(0,5)], merge_segments(s))

    @print_function_name
    @unittest.skip("reason for skipping")
    def test_merge_segments_3(self):
        s = [ (0, 1), (1,2), (2,3)]
        self.assertEqual( [(0,3)], merge_segments(s))


    @print_function_name
    @unittest.skip("reason for skipping")
    def test_merge_segments_5(self):
        s = [ (0, 1), (1,2), (2,3), (3,6), (2, 7)]
        self.assertEqual( [(0, 7)], merge_segments(s))


    @print_function_name
    @unittest.skip("reason for skipping")
    def test_merge_segments_disj(self):
        s = [ (0, 1), (3,4) ]
        self.assertEqual( s, merge_segments(s))


    @print_function_name
    @unittest.skip("reason for skipping")
    def test_merge_segments_disj_merge_left(self):
        s = [ (0,2), (1, 8), (10, 14) ]
        self.assertEqual( [(0, 8), (10,14) ], merge_segments(s))


    @print_function_name
    @unittest.skip("reason for skipping")
    def test_merge_segments_disj_merge_right(self):
        s = [ (0,2), (8, 11), (10, 14) ]
        self.assertEqual( [(0, 2), (8,14) ], merge_segments(s))

    @print_function_name
    # @unittest.skip("reason for skipping")
    def test_merge_segments_single(self):
        s = [ (2,2), (0,3)]
        # t = merge_segments(s)
        # ic(t)
        self.assertEqual( [(0, 3)], merge_segments(s))
# 
    @print_function_name
    @unittest.skip("reason for skipping")
    def test_merge_segments_single_rev(self):
        s = [(0,3), (2,2)]
        # t = merge_segments(s)
        # ic(t)
        self.assertEqual( [(0, 3)], merge_segments(s))



    @print_function_name
    @unittest.skip("reason for skipping")
    def test_merge_segment_s2_in_s1(self):
        
        inclu = merge_segment_s2_in_s1( (0, 4), (2,3) )
        ic(inclu)
        # self.assertEqual(9, man_dist(p1, p2))

        min_x = merge_segment_s2_in_s1( (0, 4), (-1,2) )
        ic(min_x)

        max_x = merge_segment_s2_in_s1( (0, 4), (1,5) )
        ic(max_x)

        disjoint = merge_segment_s2_in_s1( (0, 4), (5,7) )
        ic(disjoint)

        single = merge_segment_s2_in_s1( (2,2), (0,3) )
        ic(single)


    # @print_function_name
    # # @unittest.skip("reason for skipping")
    # def test_abscisses(self):
    #     abscisses = 
    #     self.assertEqual( [(0, 2), (8,14) ], merge_segments(s))

    @print_function_name
    # @unittest.skip("reason for skipping")
    def test_invert_segments(self):
        s = [ (0, 2), (4,5), (8, 9)]
        self.assertEqual( [(3, 3), (6, 7)], invert_segments(s) )