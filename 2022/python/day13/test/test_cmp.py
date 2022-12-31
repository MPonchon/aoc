#! venv/scripts/python.exe 
# -*- coding: utf-8 -*-

'''
    
   python3 -m unittest test.test_cmp


'''

import unittest
import sys
import os

from main import *

class TestCmp(unittest.TestCase):


    @unittest.skip("reason for skipping")
    def test_cmp_int(self):
        self.assertEqual( -1 ,  ordered([0], [5]))
        self.assertEqual( 1 ,  ordered([10], [5]))

    @unittest.skip("reason for skipping")
    def test_cmp_ints(self):
        self.assertEqual( -1 ,  ordered([0, 1], [5, 2]))
        self.assertEqual( -1 ,  ordered([0, 10], [5, 2]))


    @unittest.skip("reason for skipping")
    def test_cmp_pair1(self):
        p1 , p2 = [1,1,3,1,1], [1,1,5,1,1]
        self.assertEqual( -1 ,  ordered(p1, p2))

    @unittest.skip("reason for skipping")
    def test_cmp_pair2(self):
        p1 , p2 = [[1],[2,3,4]], [[1],4]
        self.assertEqual( -1 ,  ordered(p1, p2))

    @unittest.skip("reason for skipping")
    def test_cmp_pair3(self):
        p1 , p2 = [9], [[8,7,6]]
        self.assertEqual( -1 ,  ordered(p1, p2))

    @unittest.skip("reason for skipping")
    def test_cmp_pair4(self):
        p1 , p2 = [[4,4],4,4], [[4,4],4,4,4]
        self.assertEqual( -1 ,  ordered(p1, p2))

    @unittest.skip("reason for skipping")
    def test_cmp_pair5(self):
        p1 , p2 = [7,7,7,7] , [7,7,7]
        self.assertEqual( 1 ,  ordered(p1, p2))

    @unittest.skip("reason for skipping")
    def test_cmp_pair6(self):
        p1 , p2 = [] , [3]
        self.assertEqual( -1 ,  ordered(p1, p2))

    @unittest.skip("reason for skipping")
    def test_cmp_pair7(self):
        p1 , p2 = [[[]]] , [[]]
        self.assertEqual( 1 ,  ordered(p1, p2))

    # @unittest.skip("reason for skipping")
    def test_cmp_pair8(self):
        p1 , p2 = [1,[2,[3,[4,[5,6,7]]]],8,9] , [1,[2,[3,[4,[5,6,0]]]],8,9]
        self.assertEqual( 1 ,  ordered(p1, p2))