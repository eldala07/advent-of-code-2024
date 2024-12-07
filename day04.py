import os
import string
from collections import defaultdict
import functools
import sys
import copy
import re

#sys.setrecursionlimit(1000000)

# TEST
with open(r"input.txt") as f:
    test = f.read().strip()
    #print(s)

# REAL
with open(r"input-pt-2.txt") as f:
    real = f.read().strip()
    #print(s)

def checkRight(lines, x, y):
    if x > len(lines[y]) - 4:
        return 0
    if lines[y][x+1] == "M" and lines[y][x+2] == "A" and lines[y][x+3] == "S":
        return 1
    return 0

def checkLeft(lines, x, y):
    if x < 3:
        return 0
    if lines[y][x-1] == "M" and lines[y][x-2] == "A" and lines[y][x-3] == "S":
        return 1
    return 0

def checkTop(lines, x, y):
    if y < 3:
        return 0
    if lines[y-1][x] == "M" and lines[y-2][x] == "A" and lines[y-3][x] == "S":
        return 1
    return 0

def checkBottom(lines, x, y):
    if y > len(lines) - 4:
        return 0
    if lines[y+1][x] == "M" and lines[y+2][x] == "A" and lines[y+3][x] == "S":
        return 1
    return 0

def checkTopRight(lines, x, y):
    if y < 3 or x > len(lines[y]) - 4:
        return 0
    if lines[y-1][x+1] == "M" and lines[y-2][x+2] == "A" and lines[y-3][x+3] == "S":
        return 1
    return 0

def checkTopLeft(lines, x, y):
    if y < 3 or x < 3:
        return 0
    if lines[y-1][x-1] == "M" and lines[y-2][x-2] == "A" and lines[y-3][x-3] == "S":
        return 1
    return 0

def checkBottomRight(lines, x, y):
    if y > len(lines) - 4 or x > len(lines[y]) - 4:
        return 0
    if lines[y+1][x+1] == "M" and lines[y+2][x+2] == "A" and lines[y+3][x+3] == "S":
        return 1
    return 0

def checkBottomLeft(lines, x, y):
    if y > len(lines) - 4 or x < 3:
        return 0
    if lines[y+1][x-1] == "M" and lines[y+2][x-2] == "A" and lines[y+3][x-3] == "S":
        return 1
    return 0

def countXMASForPosition(lines, x, y):
    return checkLeft(lines, x, y) + checkRight(lines, x, y) + checkTop(lines, x, y) + checkBottom(lines, x, y) + checkTopLeft(lines, x, y) + checkTopRight(lines, x, y) + checkBottomLeft(lines, x, y) + checkBottomRight(lines, x, y)

def part_one(s):
    lines = [[char for char in line] for line in s.split("\n")]
    acc = 0
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == "X":
               acc += countXMASForPosition(lines, x, y)
    
    
    return acc


print(part_one(test))
print(part_one(real))


def checkMASBottomRight(lines, x, y):
    if y > len(lines) - 3 or x > len(lines[y]) - 3:
        return 0
    if lines[y][x] == "M":
        if lines[y+1][x+1] == "A" and lines[y+2][x+2] == "S":
            return 1
        return 0
    elif lines[y][x] == "S":
        if lines[y+1][x+1] == "A" and lines[y+2][x+2] == "M":
            return 1
        return 0
    return 0

def checkMASBottomLeft(lines, x, y):
    if y > len(lines) - 3 or x < 2 or x > len(lines[y]) - 1:
        return 0
    if lines[y][x] == "M":
        if lines[y+1][x-1] == "A" and lines[y+2][x-2] == "S":
            return 1
        return 0
    elif lines[y][x] == "S":
        if lines[y+1][x-1] == "A" and lines[y+2][x-2] == "M":
            return 1
        return 0
    return 0

def countMASForPosition(lines, x, y):
    return 1 if checkMASBottomRight(lines, x, y) + checkMASBottomLeft(lines, x+2, y) == 2 else 0

def part_two(s):
    lines = [[char for char in line] for line in s.split("\n")]
    acc = 0
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == "S" or lines[y][x] == "M":
               acc += countMASForPosition(lines, x, y)
                
    return acc


print(part_two(test))
print(part_two(real))
