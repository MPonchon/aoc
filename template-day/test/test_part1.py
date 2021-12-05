#!/usr/bin/env python3

# test_part1.py

# python -m unittest test.test_part1

import unittest

import os
from utils import loader
from part1 import *


class TestPart1(unittest.TestCase):

    def setUp(self) -> None:
        pass

    # @unittest.skip("reason for skipping")
    def test_exemple(self):
        print("* test_exemple")