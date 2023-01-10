#! /bin/env bash
day=$1
if [[ ${day:0:3} != "day" ]]; then
    echo "aoc : please issue a param that start whith 'day' !"
    exit 1
fi

cwd=$(pwd)
[[ "${cwd##*/aoc}" == "/2022/python" ]] || {
    echo "the path $cwd must be in /2022/python";
    exit 1;
}

aoc_dir="${cwd}/$1"
if [[ ! -d  ${aoc_dir} ]]; then
    mkdir "${aoc_dir}"
fi

cat << EOF >${aoc_dir}/main.py
#! /bin/env python3
#
# https://adventofcode.com/
#

from utils import add_reponse
from icecream import ic


def part1(lines):
    return 0


def part2(lines):
    return 0


def main():
    # reponse1 = 0
    # reponse2 = 0

    file_data = "exemple.txt"
    # file_data = "input.txt"

    with open(file_data, 'r') as f:
        lines = [line.strip("\n") for line in f.readlines()]

    # TODO: your code here
    # commun_part
    reponse1 = part1(lines)
    reponse2 = part2(lines)
    return reponse1, reponse2


if __name__ == "__main__":
    reponse1, reponse2 = main()

    print(f"reponse part1:{reponse1}")
    print(f"reponse part2:{reponse2}")

    add_reponse("reponse part1", reponse1)
    add_reponse("reponse part2", reponse2)

# -----------------------------
# reponse part1
# reponse part2
EOF

cat << EOF >${aoc_dir}/utils.py
#! /bin/env python3
#

def add_reponse(tag, reponse):
    """
        Ajoute la reponse en fin de fichier main
        remplace le tag par le tag + la reponse
    """
    import subprocess
    import os
    path_to_main = os.path.join(os.getcwd(), "main.py")
    if os.path.exists(path_to_main):
        command = f"sed -i 's/# {tag}.*$/# {tag}: {reponse}/g' {path_to_main}"
        subprocess.run(command, shell=True)
    else:
        print(f"Erreur chemin: {path_to_main}")

EOF


touch ${aoc_dir}/exemple.txt
touch ${aoc_dir}/input.txt

# test files

if [[ ! -d  ${aoc_dir}/test ]]; then
    mkdir "${aoc_dir}/test"
fi

touch ${aoc_dir}/test/__init__.py

cat << EOF >${aoc_dir}/test/wrappers.py
#! venv/scripts/python.exe 
# -*- coding: utf-8 -*-
"""
    Helpers decorators
"""
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

EOF

cat << EOF >${aoc_dir}/test/test_one.py
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

EOF