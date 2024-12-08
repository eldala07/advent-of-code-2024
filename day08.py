import os
import string
from collections import defaultdict
import functools
import sys
import copy
import re
import math
import time

#sys.setrecursionlimit(1000000)

# TEST
with open(r"input.txt") as f:
    test = f.read().strip()
    #print(s)

# REAL
with open(r"input-pt-2.txt") as f:
    real = f.read().strip()
    #print(s)

def execute_and_elapsed_time(fn, text):
    tic = time.time()
    fn()
    toc = time.time()
    elapsed_time = toc - tic
    print(f"Elapsed time {text}: {elapsed_time:.2f} seconds")

def scan(lines):
    letters_pos = {}
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            letter = lines[y][x]
            if letter != ".":
                if letter not in letters_pos:
                    letters_pos[letter] = [[y, x]]
                else:
                    letters_pos[letter].append([y, x])
    return letters_pos

def is_valid_antinode(lines, antinode):
    min_y = 0
    min_x = 0
    max_y = len(lines) - 1
    max_x = len(lines[0]) - 1
    if antinode[0] < min_y or antinode[0] > max_y:
        return False
    if antinode[1] < min_x or antinode[1] > max_x:
        return False
    # if lines[antinode[0]][antinode[1]] != ".":
        # return False
    return True
    

def get_antinodes_for_pair(lines, pos_1, pos_2):
    diff_y = (pos_2[0] - pos_1[0])
    diff_x = (pos_2[1] - pos_1[1])
    antinode_1 = [pos_1[0] - diff_y, pos_1[1] - diff_x]
    antinode_2 = [pos_2[0] + diff_y, pos_2[1] + diff_x]
    valid_antinodes = []
    if is_valid_antinode(lines, antinode_1):
        valid_antinodes.append(antinode_1)
    if is_valid_antinode(lines, antinode_2):
        valid_antinodes.append(antinode_2)
    return valid_antinodes

def compute_antinodes(lines, letters_pos, version):
    antinodes = set()
    for letter, positions in letters_pos.items():
        for i, pos_1 in enumerate(positions):
            for j in range(i + 1, len(positions)):
                pos_2 = positions[j]
                if version == "2": 
                    valid_antinodes = get_antinodes_for_pair_part_2(lines, pos_1, pos_2)
                else:
                    valid_antinodes = get_antinodes_for_pair(lines, pos_1, pos_2)
                for antinode in valid_antinodes:
                    antinodes.add(str(antinode))

    return antinodes

def part_one(s):
    lines = [[char for char in x] for x in s.splitlines()]
    letters_pos = scan(lines)
    antinodes = compute_antinodes(lines, letters_pos, "1")
    return len(antinodes)

execute_and_elapsed_time(lambda: print(part_one(test)), "part 1 test")
execute_and_elapsed_time(lambda: print(part_one(real)), "part 1 real")

# 23257 too high

def get_antinodes_for_pair_part_2(lines, pos_1, pos_2):
    diff_y = (pos_2[0] - pos_1[0])
    diff_x = (pos_2[1] - pos_1[1])
    antinodes = []
    antinodes.append(pos_1)
    antinodes.append(pos_2)
    antinode_1 = [pos_1[0] - diff_y, pos_1[1] - diff_x]
    antinode_2 = [pos_2[0] + diff_y, pos_2[1] + diff_x]
    antinodes.append(antinode_1)
    antinodes.append(antinode_2)
    
    valid_antinodes = []
    
    i = 2
    while antinode_1[0] >= 0 and antinode_1[1] >= 0 and antinode_1[0] <= len(lines) and antinode_1[1] <= len(lines[0]):
        antinode_1 = [pos_1[0] - i * diff_y, pos_1[1] - i * diff_x]
        if is_valid_antinode(lines, antinode_1):
            valid_antinodes.append(antinode_1)
        i += 1

    j = 2
    while antinode_2[0] >= 0 and antinode_2[1] >= 0 and antinode_2[0] <= len(lines) and antinode_2[1] <= len(lines[0]):
        antinode_2 = [pos_2[0] + j * diff_y, pos_2[1] + j * diff_x]
        if is_valid_antinode(lines, antinode_2):
            valid_antinodes.append(antinode_2)
        j += 1
        
    for antinode in antinodes:
        if is_valid_antinode(lines, antinode):
            valid_antinodes.append(antinode)
    return valid_antinodes

def part_two(s):
    lines = [[char for char in x] for x in s.splitlines()]
    letters_pos = scan(lines)
    antinodes = compute_antinodes(lines, letters_pos, "2")
    return len(antinodes) 

execute_and_elapsed_time(lambda: print(part_two(test)), "part 2 test")
execute_and_elapsed_time(lambda: print(part_two(real)), "part 2 real")

