#! venv/scripts/python.exe 
# -*- coding: utf-8 -*-

'''
   python3 -m unittest test.test_segment
'''

import unittest
import sys
import os
from icecream import ic

from main import Segment

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


class TestSegment(unittest.TestCase):


    @print_function_name
    # @unittest.skip("reason for skipping")
    def test_contains(self):
        s1 = Segment(5, 8)
        s2 = Segment(5, 6)

        self.assertTrue(s1.__contains__(6))
        self.assertTrue(s1.__contains__(s2))
        # if s2 in s1:    ic('ok')

        self.assertFalse(s1.__contains__(Segment(7, 9)))
        self.assertFalse(s1.__contains__(Segment(4, 6)))
        self.assertFalse(s1.__contains__(Segment(4, 9)))

    @print_function_name
    # @unittest.skip("reason for skipping")
    def test_merge(self):
        s1 = Segment(5, 8)
        self.assertEqual(True, s1.merge(Segment(4,5)))
        self.assertEqual(4, s1.left)
        self.assertEqual(8, s1.right)

        s1 = Segment(5, 8) # inclus
        self.assertEqual(True, s1.merge(Segment(5,6)))
        self.assertEqual(5, s1.left)
        self.assertEqual(8, s1.right)

        s1 = Segment(5, 8) # inclus
        self.assertEqual(True, s1.merge(Segment(5,9)))
        self.assertEqual(5, s1.left)
        self.assertEqual(9, s1.right)

        s1 = Segment(4, 5)
        self.assertEqual(True, s1.merge(Segment(5, 8)))
        self.assertEqual(4, s1.left)
        self.assertEqual(8, s1.right)

        s1 = Segment(5, 6) # inclus
        self.assertEqual(True, s1.merge(Segment(5, 8)))
        self.assertEqual(5, s1.left)
        self.assertEqual(8, s1.right)


        s1 = Segment(4, 5)
        self.assertEqual(False, s1.merge(Segment(6, 8)))
        self.assertEqual(4, s1.left)
        self.assertEqual(5, s1.right)