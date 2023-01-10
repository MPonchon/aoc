#! venv/scripts/python.exe 
# -*- coding: utf-8 -*-
'''
   python3 -m unittest test.test_one
'''

from test.wrappers import print_function_name
import unittest

import sys
import os

from main import *

class TestCmp(unittest.TestCase):

    @print_function_name
    @unittest.skip("reason for skipping")
    def test_casewherefunctiondosomething(self):
        # self.assertEqual(expected, functiondosomething())

