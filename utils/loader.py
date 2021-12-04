#!/usr/bin/python3

# loader.py

def load_data(path_to_file: str) -> list:
    flines = []
    with open(path_to_file, 'r') as f:
        flines = f.readlines()

    lines = [line.strip("\r\n") for line in flines]
    return lines

