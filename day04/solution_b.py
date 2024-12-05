#!/usr/bin/env python3
import sys

def main():
    grid = []
    for line in sys.stdin:
        grid += [list(line.strip())]
    
    count = 0

    for y in range(1, len(grid)-1):
        for x in range(1, len(grid[0])-1):
            if grid[y][x] == 'A':
                d1 = sorted([grid[y-1][x-1], grid[y+1][x+1]])
                d2 = sorted([grid[y-1][x+1], grid[y+1][x-1]])
                if d1 == ['M', 'S'] and d2 == ['M', 'S']:
                    count += 1

    print(count)

if __name__ == '__main__':
    main()