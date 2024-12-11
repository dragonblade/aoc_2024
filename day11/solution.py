#!/usr/bin/env python3

import math


HIST = {}


def read():
    return list(map(int, input().strip().split()))


def a(stones: list[int]):
    print(sum(blink(25, s) for s in stones))


def b(stones: list[int]):
    print(sum(blink(75, s) for s in stones))


def blink(n: int, s: int) -> int:
    r: int
    if (n, s) in HIST:
        return HIST[(n, s)]
    elif n == 0:
        return 1
    elif s == 0:
        r = blink(n - 1, 1)
    elif num_digits(s) % 2 == 0:
        c = num_digits(s) // 2
        r = blink(n - 1, s % 10**c) + blink(n - 1, s // 10**c)
    else:
        r = blink(n - 1, s * 2024)
    HIST[(n, s)] = r
    return r


def num_digits(n: int) -> int:
    return math.floor(math.log10(n) + 1)


if __name__ == "__main__":
    stones = read()
    a(stones)
    b(stones)
