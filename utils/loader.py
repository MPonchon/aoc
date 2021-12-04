#!/usr/bin/env python3

# loader.py

import os
def get_project_root(project_name: str) -> str:
    file_path = os.path.dirname(os.path.abspath(__file__))
    if project_name not in file_path:
        return ""
    pos = file_path.index(project_name) + len(project_name)
    return file_path[:pos] + os.path.sep

# import sys
ROOT_DIR = get_project_root("aoc")
# sys.path.append(ROOT_DIR)


def load_data(path_to_file: str) -> list:
    flines = []
    with open(path_to_file, 'r') as f:
        flines = f.readlines()

    lines = [line.strip("\r\n") for line in flines]
    return lines

