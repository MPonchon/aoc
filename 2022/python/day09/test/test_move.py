#! venv/scripts/python.exe 
# -*- coding: utf-8 -*-

'''
    
   python -m unittest test.test_move


'''

import unittest
import sys


import os

from main import *

class TestMove(unittest.TestCase):

    @unittest.skip("reason for skipping")
    def test_move_R(self):
        tail = (0,0)
        head = (0,0)
        self.assertEqual( (0,0),  move_tail(head, tail))

        head = (1,0)
        self.assertEqual( (0,0),  move_tail(head, tail))

        head = (2,0)
        self.assertEqual( (1,0),  move_tail(head, tail))

    @unittest.skip("reason for skipping")
    def test_move_R_delta_2(self):
        tail = (1,0)
        head = (3,0)
        self.assertEqual( (2,0),  move_tail(head, tail))


    @unittest.skip("reason for skipping")
    def test_move_U_delta_2(self):
        tail = (3,-2)
        head = (3,0)
        self.assertEqual( (3, -1),  move_tail(head, tail))


    @unittest.skip("reason for skipping")
    def test_move_U_decale_2(self):
        tail = (1, 1)
        head = (2, 3)
        self.assertEqual( (2, 2),  move_tail(head, tail))


    @unittest.skip("reason for skipping")
    def test_move_R_decale_2(self):
        tail = (1, 1)
        head = (3, 2)
        self.assertEqual( (2, 2),  move_tail(head, tail))
