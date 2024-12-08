#!/usr/bin/env python3
import sys

def read() -> list[list[str]]:
    grid = []
    for line in sys.stdin:
        grid.append(list(line.strip()))
    return grid

def a(grid: list[list[str]]):
    antinodes: list[tuple[int, int]] = []
    nodes: dict[str, list[tuple[int, int]]] = {}

    my, mx = len(grid), len(grid[0])

    for y in range(my):
        for x in range(mx):
            if grid[y][x] != '.':
                ant = grid[y][x]
                if ant not in nodes:
                    nodes[ant] = []
                nodes[ant].append((y, x))

    for ants in nodes.values():
        for ya, xa in ants:
            for yb, xb in ants:
                if (ya, xa) != (yb, xb):
                    yc, xc = yb + (yb - ya), xb + (xb - xa)
                    if 0 <= yc < my and 0 <= xc < mx and (yc, xc) not in antinodes:
                        antinodes.append((yc, xc))

    print(len(antinodes))

def b(grid: list[list[str]]):
    antinodes: list[tuple[int, int]] = []
    nodes: dict[str, list[tuple[int, int]]] = {}

    my, mx = len(grid), len(grid[0])

    for y in range(my):
        for x in range(mx):
            if grid[y][x] != '.':
                ant = grid[y][x]
                if ant not in nodes:
                    nodes[ant] = []
                nodes[ant].append((y, x))
    
    for ants in nodes.values():
        for ya, xa in ants:
            for yb, xb in ants:
                if (ya, xa) != (yb, xb):
                    yd, xd = (yb - ya), (xb - xa)
                    yc, xc = yb, xb
                    while 0 <= yc < my and 0 <= xc < mx:
                        if (yc, xc) not in antinodes:
                            antinodes.append((yc, xc))
                        yc, xc = yc + yd, xc + xd

    print(len(antinodes))


if __name__ == '__main__':
    grid = read()
    a(grid)
    b(grid)
