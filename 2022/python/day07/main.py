#! /bin/env python3
#
# https://adventofcode.com/
#

from icecream import ic

data = open("input.txt", "r", encoding="utf-8").read().splitlines()

fs = [] #['/a/b/c/file|dir, size'],[...],[...]
filepath = []

for d in data:
    a = d.strip().split()
    if a[0] == '$':
        if a[1] =='cd':
            if a[2] == '..':
                filepath.pop()
            else:
                if a[2] == '/': a[2]=''
                filepath.append(a[2] + '/')
    elif a[0] == 'dir':
        fs.append([''.join(map(str,filepath)) + a[1] + '/' , 0        ])
    else:
        fs.append([''.join(map(str,filepath)) + a[1]       , int(a[0])])

fs.sort()
# for f in fs:
#     print(*f)

'''PART 01'''
total=0
grandtotal=0
for a,b in fs:
    if a[-1:]=='/': # directory
        for c,d in fs:
            if c.find(a) != -1 : # this file lives inside the directory
                total+=d
        if total<=100000:
            grandtotal+=total
            print(a, total)
        total=0
print('part 01: ',grandtotal)

'''PART 02'''
total=0
grandtotals=[]
for a,b in fs:
    if a[-1:]=='/': # directory
        for c,d in fs:
            if c.find(a) != -1 : # this file lives inside the directory
                total+=d
        grandtotals.append(total)
        total=0

grandtotals.sort()

used = sum(b for a,b in fs)
free = 70000000 - used
todelete = 30000000 - free

for g in grandtotals:
    if g >= todelete:
        print('part 02: ',g)
        break