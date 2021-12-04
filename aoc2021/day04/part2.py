#!/usr/bin/python3

# part2.py

"""
--- Part Two ---

On the other hand, it might be wise to try a different strategy: let the giant squid win.

You aren't sure how many bingo boards a giant squid could play at once, 
so rather than waste time counting its arms, 
the safe thing to do is to figure out which board will win last and choose that one.

That way, no matter which boards it picks, it will win for sure.

In the above example, 
the second board is the last to win,
which happens after 13 is eventually called 
and its middle column is completely marked. 

If you were to keep playing until this point, 
the second board would have a sum of unmarked numbers equal to 148 
for a final score of 148 * 13 = 1924.

Figure out which board will win last. Once it wins, what would its final score be?

24
22   13  17M 11M  0M         3  15   0M  2M 22         14M 21M 17M 24M  4M
 8   2M  23M  4M 24M         9M 18  13  17M  5M        10  16  15   9M 19
21M  9M  14M 16   7M        19   8   7M 25  23M        18   8  23M 26  20
 6  10   3   18   5M        20  11M 10  24M  4M        22  11M 13   6   5M
 1  12  20   15  19         14M 21M 16  12   6          2M  0M 12   3   7M

7,4,9,5,11,17,23,2,0,14,21,24, 10,16,13

10
22   13  17M 11M  0M         3  15   0M  2M 22         14M 21M 17M 24M  4M
 8   2M  23M  4M 24M         9M 18  13  17M  5M        10A 16  15   9M 19
21M  9M  14M 16   7M        19   8   7M 25  23M        18   8  23M 26  20
 6  10A  3   18   5M        20  11M 10A 24M  4M        22  11M 13   6   5M
 1  12  20   15  19         14M 21M 16  12   6          2M  0M 12   3   7M

16
22   13  17M 11M  0M         3  15   0M  2M 22         14M 21M 17M 24M  4M
 8   2M  23M  4M 24M         9M 18  13  17M  5M        10A 16B 15   9M 19
21M  9M  14M 16B  7M        19   8   7M 25  23M        18   8  23M 26  20
 6  10A  3   18   5M        20  11M 10A 24M  4M        22  11M 13   6   5M
 1  12  20   15  19         14M 21M 16B 12   6          2M  0M 12   3   7M



"""
import os

from utils import loader
from part1 import check_win_grille, read_numbers, read_grilles, sum_unmarked


def last_win(grilles: dict, numbers: list, marks: set) -> int:
    """
    trouve le dernier board gagnant
    retroune le no de board, le numero sorti
    """
    # marks = set()
    boad_won = set()
    for n in numbers:
        # print("numero:", n)
        if n in marks:
            continue
        marks.add(n)
        for key, grille in grilles.items():
            if check_win_grille(grille, marks):
                # print("key: {}, boad_won:{}".format(key, boad_won))
                if key not in boad_won:
                    # print("key: {} not in board".format(key))
                    if len(boad_won) == len(grilles.keys()) - 1:
                        # print("->boad_won:", boad_won, n , key)
                        return key, n
                boad_won.add(key)
    return 0


if __name__ == "__main__":
    print("AOC: part2")

    # get data
    path_to_file = os.path.join(os.getcwd(), 'data.txt')
    # path_to_file = os.path.join(os.getcwd(), 'exemple.txt')
    data = loader.load_data(path_to_file)

    nums = read_numbers(data)
    grilles = read_grilles(data[1:])

    marks = set()

    n_board, num = last_win(grilles, nums, marks)
    print("board, num: ", n_board, num)
    sum = sum_unmarked(grilles[n_board], marks)
    print(sum)
    result = num * sum
    print(result)
    # board, num:  42 59
    # 170
    # 10030
