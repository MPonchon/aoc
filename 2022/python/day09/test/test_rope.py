#! venv/scripts/python.exe 
# -*- coding: utf-8 -*-

'''
    
   python -m unittest test.test_rope


'''

import unittest
import sys


import os

from main import *

class TestRope(unittest.TestCase):

    # @unittest.skip("reason for skipping")
    def test_move_R(self):
        # self.assertEqual( (0,0),  move_tail(head, tail))

        # rope = [(0, 0) for i in range(9)]
        # head = (2,0)
        # rope[0] = move_tail(head, rope[0])
        # ic (rope)

        # rope = [(0, 0) for i in range(9)]
        # rope[0] = (2, 0)
        # ic (rope)
        # head = (4,0)
        # rope[0] = move_tail(head, rope[0])
        # ic (rope)
        kt = (0,0)
        kh = (0,0)
        head = (2,0)
        self.assertEqual( (1,0),  move_tail(head, kh))

        kt = (0,0)
        kh = (1,0)
        head = (3,0)
        self.assertEqual( (2,0),  move_tail(head, kh))
