import os
import string
from collections import defaultdict
import functools
import sys

#sys.setrecursionlimit(1000000)
dirs = ((-1, 0), (0, 1), (1, 0), (-1, 0))
dirs3 = ()

with open(r"input.txt") as f:
    s = f.read().strip()
    # print(s)

vectors = [[int(y) for y in x.split("x")] for x in s.split("\n")]
# print(vectors)

def part_one(vec):
    dummy_var = 0
    return dummy_var

def part_two(vec):
    dummy_var = 0
    return dummy_var

print(part_one(vectors))
print(part_two(vectors))
