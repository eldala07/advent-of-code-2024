import os
import string
from collections import defaultdict
import functools
import sys
import copy

# sys.setrecursionlimit(1000000)

# TEST
with open(r"input.txt") as f:
    test = f.read().strip()
    # print(s)

# REAL
with open(r"input-pt-2.txt") as f:
    real = f.read().strip()
    # print(s)

MAX_DIST = 3


def analyze_sequence(x):
    direction = None
    safe = True
    index_issue = None

    for index, y in enumerate(x):
        if index == len(x) - 1:
            return safe, direction, index_issue

        if index == 0:
            if x[index] - x[index + 1] < 0:
                direction = "desc"
            elif x[index] - x[index + 1] > 0:
                direction = "asc"

        if direction is None:
            safe = False
            index_issue = index
            break

        if direction == "desc" and x[index] - x[index + 1] >= 0:
            safe = False
            index_issue = index
            break

        if direction == "asc" and x[index] - x[index + 1] <= 0:
            safe = False
            index_issue = index
            break

        if not (0 < abs(x[index] - x[index + 1]) <= 3):
            safe = False
            index_issue = index
            break

    return safe, direction, index_issue


def part_one(s):
    array_of_values = [[int(y) for y in x.split(" ")] for x in s.split("\n")]

    result_arr = []
    nb_of_safe = 0
    for x in array_of_values:
        [safe, direction, _] = analyze_sequence(x)
        if safe:
            nb_of_safe += 1

    return nb_of_safe


print(part_one(test))
print(part_one(real))


def part_two(s):
    array_of_values = [[int(y) for y in x.split(" ")] for x in s.split("\n")]

    nb_of_safe = 0
    for x in array_of_values:
        [safe, direction, index_issue] = analyze_sequence(x)
        if safe:
            nb_of_safe += 1
        elif not safe:
            for index, y in enumerate(x):
                deep_copy = copy.deepcopy(x)
                del deep_copy[index]
                [safe2, direction2, _] = analyze_sequence(deep_copy)

                if safe2:
                    nb_of_safe += 1
                    break

    return nb_of_safe
