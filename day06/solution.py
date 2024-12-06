#!/usr/bin/env python3
import copy
import sys

def read() -> list[list[str]]:
    grid = []
    for line in sys.stdin:
        grid.append(list(line.strip()))
    return grid

def a(grid: list[list[str]]):
    y, x = 0, 0
    dir = '^'
    for j, line in enumerate(grid):
        if '^' in line:
            y = j
            x = line.index('^')
    
    count = 1

    while True:
        ny, nx = move(y, x, dir)
        while 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and grid[ny][nx] == '#':
            dir = turn(dir)
            ny, nx = move(y, x, dir)
        
        y, x = ny, nx
        if not (0 <= nx < len(grid[0]) and 0 <= ny < len(grid)):
            break
        if 'X' not in grid[y][x] and '^' not in grid[y][x]:
            count += 1
        grid[y][x] = 'X'

    print(count)

def b(grid: list[list[str]]):
    y, x = 0, 0
    dir = '^'
    for j, line in enumerate(grid):
        if '^' in line:
            y = j
            x = line.index('^')

    vis = [(y, x)]
    placed = []
    count = 0

    while True:
        ny, nx = move(y, x, dir)
        while 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and grid[ny][nx] == '#':
            dir = turn(dir)
            ny, nx = move(y, x, dir)
        
        if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
            newgrid = copy.deepcopy(grid)
            newgrid[ny][nx] = 'O'

            if (ny, nx) not in vis:
                if hasloop(newgrid, y, x, dir):
                    if (ny, nx) not in placed:
                        placed += [(ny, nx)]
                        count += 1
        else:
            break
        y, x = ny, nx
        vis.append((y, x))

    print(count)

def hasloop(grid: list[list[str]], y: int, x: int, dir: str) -> bool:
    vis = [(y, x, dir)]
    while True:
        ny, nx = move(y, x, dir)
        while 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and (grid[ny][nx] == '#' or grid[ny][nx] == 'O'):
            dir = turn(dir)
            ny, nx = move(y, x, dir)

        if not (0 <= nx < len(grid[0]) and 0 <= ny < len(grid)):
            return False
        y, x = ny, nx
        if (y, x, dir) in vis:
            return True
        vis += [(y, x, dir)]


def move(y: int, x: int, dir: str) -> tuple[int, int]:
    if dir == '^':
        return (y-1, x)
    elif dir == '>':
        return (y, x+1)
    elif dir == '<':
        return (y, x-1)
    elif dir == 'v':
        return (y+1, x)

def turn(dir: str) -> str:
    match dir:
        case '^': return '>'
        case '>': return 'v'
        case 'v': return '<'
        case '<': return '^'

if __name__ == '__main__':
    grid = read()
    a(copy.deepcopy(grid))
    b(grid)
