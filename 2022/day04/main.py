#! /bin/env python3

from icecream import ic

def data_to_set(part: str) -> set:
    deb, fin = part.split('-')
    ret_set= set()
    for i in range(int(deb), int(fin)+1):
        ret_set.add(i)
    return ret_set

def main():
    # file_data="exemple.txt"
    file_data="input.txt"
# 
    with open(file_data , 'r') as f:
        lines = [line.strip("\n")  for line in f.readlines()]

        sum_pairs_contains = 0
        sum_overlaps = 0
        for line in lines:
            p1, p2 = line.split(',')
            # ic(p1)
            s1 = data_to_set(p1)
            # ic(s1)
            s2 = data_to_set(p2)
            if s1.issubset(s2) or s2.issubset(s1):
                sum_pairs_contains +=1

            if s1.intersection(s2) or s2.intersection(s1):
                sum_overlaps +=1
            
        print(f"sum_pairs_contains:{sum_pairs_contains}")
        print(f"sum_overlaps:{sum_overlaps}")

if __name__ == "__main__":
        main()
