#! venv/scripts/python.exe 
# -*- coding: utf-8 -*-

'''
    
   python -m unittest test.test_win


'''

import unittest
import sys


import os

from main import win_or_loss
from main import ROCK, PAPER, SCISSOR

class dbTeTestWinst(unittest.TestCase):

    # @unittest.skip("reason for skipping")
    def test_win1(self):
        print('-test: test_win1')
        self.assertEqual(2 , win_or_loss(ROCK, ROCK))
        self.assertEqual(8 , win_or_loss(ROCK, PAPER))
        self.assertEqual(1 , win_or_loss(ROCK, SCISSOR))

        self.assertEqual(1 , win_or_loss(PAPER, ROCK))
        self.assertEqual(4 , win_or_loss(PAPER, PAPER))
        self.assertEqual(9 , win_or_loss(PAPER, SCISSOR))

        self.assertEqual(7 , win_or_loss(SCISSOR, ROCK))
        self.assertEqual(1 , win_or_loss(SCISSOR, PAPER))
        self.assertEqual(6 , win_or_loss(SCISSOR, SCISSOR))