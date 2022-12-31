from collections import deque
from math import inf as INFINITY
from icecream import ic

def bfs(grid, src, dst):
    h, w    = len(grid), len(grid[0]) # pre-calculate height and width for simplicity
    queue   = deque([(0, src)])       # queue of tuples (distance_from_src, coords)
    visited = set()

    # While there are coordinates to visit
    while queue:
        # Get the first one in the queue
        distance, rc = queue.popleft()
        # If we reached the desination, return the distance traveled so far
        ic(queue)
        if rc == dst:
            return distance

        # Skip already vsited coordinates
        if rc not in visited:
            visited.add(rc)

            # For each neighboring cell that wasn't already visited
            for n in get_neighbors(grid, r, c, h, w):
                if n in visited:
                    continue

                # Add it to the back of the queue with a distance equal to the
                # current one plus 1
                queue.append((distance + 1, n))

    return INFINITY

def get_neighbors(grid, r, c, h, w): # get h, w as parameters for simplicity
    max_el = grid[r][c] + 1

    for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
        if 0 <= nr < h and 0 <= nc < w: # ensure we are within the grid
            if grid[nr][nc] <= max_el:  # ensure this neighbor is reachable
                yield nr, nc


file_data = "exemple.txt"
# file_data = "input.txt"


with open(file_data, 'rb') as fin:
    lines = fin.read().splitlines()
    grid = list(map(list, lines))

ic(grid)

# These will all be ints since iterating bytes yields ints
START, END, LOWEST, HIGHEST = b'SEaz'

src = dst = None

for r, row in enumerate(grid):
    for c, cell in enumerate(row):
        if cell == START:
            src = r, c
            grid[r][c] = LOWEST
        elif cell == END:
            dst = r, c
            grid[r][c] = HIGHEST

    if src and dst:
        break
ic(src, dst)

min_dist = bfs(grid, src, dst)

print('Part 1:', min_dist)