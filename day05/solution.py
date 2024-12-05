#!/usr/bin/env python3
import sys

def read() -> tuple[list[list[int]], list[list[int]]]:
    rules: list[list[int]] = []
    prints: list[list[int]] = []
    for line in sys.stdin:
        if '|' in line:
            rules.append(list(map(int, line.split('|'))))
        elif ',' in line:
            prints.append(list(map(int, line.split(','))))
    
    return rules, prints

def a(rules: list[list[int]], prints: list[list[int]]):
    middles = []

    for sample in prints:
        valid = True
        for rule in rules:
            left, right = rule
            if left in sample and right in sample and sample.index(left) > sample.index(right):
                valid = False
        
        if valid:
            middles.append(sample[len(sample)//2])
    
    print(sum(middles))

def b(rules: list[list[int]], prints: list[list[int]]):
    middles = []

    for sample in prints:
        valid = True
        repeat = True
        while repeat:
            repeat = False
            for rule in rules:
                left, right = rule
                if left in sample and right in sample and sample.index(left) > sample.index(right):
                    valid = False
                    repeat = True
                    lidx, ridx = sample.index(left), sample.index(right)
                    sample[lidx], sample[ridx] = sample[ridx], sample[lidx]
                    break
        
        if not valid:
            middles.append(sample[len(sample)//2])

    print(sum(middles))

if __name__ == '__main__':
    rules, prints = read()
    a(rules, prints)
    b(rules, prints)
