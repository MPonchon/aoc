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


class TestCmp(unittest.TestCase):

    @print_function_name
    @unittest.skip("reason for skipping")
    def test_cmp_both_int(self):
        p1 = 0
        p2 = 5
        self.assertEqual( -1 ,  ordered(p1, p2))

