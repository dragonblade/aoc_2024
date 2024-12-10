#!/usr/bin/env python3

import sys


def read() -> list[list[int]]:
    grid = []
    for line in sys.stdin:
        grid.append(list(map(int, list(line.strip()))))
    return grid


def a(grid: list[list[int]]):
    sum = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            sum += len(set(reachable(grid, -1, y, x)))
    print(sum)


def reachable(
    grid: list[list[int]], current: int, y: int, x: int
) -> list[tuple[int, int]]:
    if (
        y < 0
        or y >= len(grid)
        or x < 0
        or x >= len(grid[y])
        or grid[y][x] != current + 1
    ):
        return []
    elif grid[y][x] == 9:
        return [(y, x)]
    return (
        reachable(grid, grid[y][x], y, x - 1)
        + reachable(grid, grid[y][x], y, x + 1)
        + reachable(grid, grid[y][x], y - 1, x)
        + reachable(grid, grid[y][x], y + 1, x)
    )


def b(grid: list[list[int]]):
    sum = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            sum += rating(grid, -1, y, x)
    print(sum)


def rating(grid: list[list[int]], current: int, y: int, x: int) -> int:
    if (
        y < 0
        or y >= len(grid)
        or x < 0
        or x >= len(grid[y])
        or grid[y][x] != current + 1
    ):
        return 0
    elif grid[y][x] == 9:
        return 1
    return (
        rating(grid, grid[y][x], y, x - 1)
        + rating(grid, grid[y][x], y, x + 1)
        + rating(grid, grid[y][x], y - 1, x)
        + rating(grid, grid[y][x], y + 1, x)
    )


if __name__ == "__main__":
    grid = read()
    a(grid)
    b(grid)
