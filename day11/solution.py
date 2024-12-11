#!/usr/bin/env python3

import math


def read():
    return list(map(int, input().strip().split()))


def a(stones: list[int]):
    for _ in range(25):
        stones = blink(stones)
    print(len(stones))


def b(stones: list[int]):
    for _ in range(75):
        stones = blink(stones)
    print(len(stones))


def blink(stones: list[int]) -> list[int]:
    new = []
    for stone in stones:
        if stone == 0:
            new.append(1)
        elif math.floor(math.log10(stone) + 1) % 2 == 0:
            c = math.floor(math.log10(stone) + 1) // 2
            new += [stone % 10**c, stone // 10**c]
        else:
            new.append(stone * 2024)
    return new


if __name__ == "__main__":
    stones = read()
    a(stones)
    b(stones)
