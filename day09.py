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

def get_file_blocks(dm):
    block_files = []
    for index, value in enumerate(dm):
        if index % 2 == 0:
            for i in range(value):
                block_files.append(int(index/2))
        else:
            for i in range(value):
                block_files.append(-1)

    return block_files

def is_valid_filesystem(filesystem):
    is_valid = True
    nb_gaps = 0
    for bf in filesystem:
        if bf == -1:
            if nb_gaps >= 1:
                is_valid = False
                break
        elif bf != -1:
            nb_gaps += 1

    return is_valid

def rearrange_blocks(block_files):
    copy_blocks = block_files.copy()
    reversed_block_files = block_files.copy()[::-1]
    for i, rbf in enumerate(reversed_block_files):
        if rbf == -1:
            continue
        index_to_replace = copy_blocks.index(-1)
        copy_blocks[index_to_replace] = rbf
        copy_blocks[-i-1] = -1
        reversed_block_files[i] = -1
        if is_valid_filesystem(copy_blocks[::-1]):
            break
    return copy_blocks

def get_filesystem_checksum(rearranged_block_files):
    checksum = 0
    for i, bf in enumerate(rearranged_block_files):
        if bf == -1:
            continue
        checksum += bf * i
    return checksum



def part_one(s):
    disk_map = [[int(char) for char in x] for x in s.splitlines()][0]
    block_files = get_file_blocks(disk_map)
    rearranged_blocks = rearrange_blocks(block_files)
    checksum = get_filesystem_checksum(rearranged_blocks)
    return checksum

execute_and_elapsed_time(lambda: print(part_one(test)), "part 1 test")
execute_and_elapsed_time(lambda: print(part_one(real)), "part 1 real")

def get_block(block_files, start_index):
    bf = block_files[start_index]
    init_bf = bf
    end_index = start_index
    i = 1
    while bf == init_bf and end_index < len(block_files) - 1:
        end_index += 1
        bf = block_files[start_index+i]
        i = i+1
    end_index -= 1
    length = end_index - start_index + 1
    return start_index, end_index, length

def get_indexes_to_replace(block_files, length, stop_index):
    indexes_to_replace = []
    found = False
    length_found = 0
    for i, bf in enumerate(block_files):
        if i == stop_index:
            found = False
            length_found = 0
            indexes_to_replace = []
            break
        if bf == -1:
            found = True
            length_found += 1
            indexes_to_replace.append(i)
            if length_found == length:
                break
        else:
            if found:
                found = False
                length_found = 0
                indexes_to_replace = []
    return indexes_to_replace
    

def rearrange_blocks_p2(block_files):
    copy_blocks = block_files.copy()
    reversed_block_files = block_files.copy()[::-1]

    nb_skips = 0
    for i, rbf in enumerate(reversed_block_files):
        if nb_skips > 0:
            nb_skips -= 1
            continue
        if rbf == -1:
            continue
        start_index, end_index, length = get_block(reversed_block_files, i)
        stop_index = len(reversed_block_files) - 1 - end_index
        nb_skips = length - 1
        indexes_to_replace = get_indexes_to_replace(copy_blocks, length, stop_index)
        if len(indexes_to_replace) == 0:
            continue
        for index_to_replace in indexes_to_replace:
            copy_blocks[index_to_replace] = rbf
        for index in range(start_index, end_index + 1):
            reversed_block_files[index] = -1
            copy_blocks[-index-1] = -1
    return copy_blocks

def part_two(s):
    disk_map = [[int(char) for char in x] for x in s.splitlines()][0]
    block_files = get_file_blocks(disk_map)
    rearranged_blocks = rearrange_blocks_p2(block_files)
    checksum = get_filesystem_checksum(rearranged_blocks)
    return checksum       

execute_and_elapsed_time(lambda: print(part_two(test)), "part 2 test")
execute_and_elapsed_time(lambda: print(part_two(real)), "part 2 real")

