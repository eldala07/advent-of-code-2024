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

def is_current_position_close_to_block(y, x, next_move):
    if next_move[0] == y and next_move[1] == x:
        return True
    return False

def get_guard_position_and_first_move(lines):
    next_move = [0, 0]
    guard_y = 0
    guard_x = 0
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == "<":
                guard_y = y
                guard_x = x
                next_move = [0, -1]
                break
            elif lines[y][x] == ">":
                guard_y = y
                guard_x = x
                next_move = [0, 1]
                break
            elif lines[y][x] == "^":
                guard_y = y
                guard_x = x
                next_move = [-1, 0]
                break
            elif lines[y][x] == "v":
                guard_y = y
                guard_x = x
                next_move = [1, 0]
                break
                
    return guard_y, guard_x, next_move

def can_move(lines, y, x, next_move, y_block, x_block, loop_count, visited_blocking):
    try: 
        if y+next_move[0] > len(lines)-1 or y+next_move[0] < 0:
            return "end"
        if x+next_move[1] > len(lines[y+next_move[0]])-1 or x+next_move[1] < 0:
            return "end"
        if lines[y+next_move[0]][x + next_move[1]] == "#":
            pos = str(y+next_move[0]) + "," + str(x + next_move[1])
            direction = str(next_move[0]) + "," + str(next_move[1])
            key = pos + "/" + direction
            if key in visited_blocking:
                    loop_count[0] = 2
            else:
                visited_blocking[key] = 1
                    
            return "no"
    except IndexError:
        return "end"
    return "yes"

def get_next_move(lines, y, x, next_move, y_block, x_block, loop_count, visited_blocking):
    can_move_result = can_move(lines, y, x, next_move, y_block, x_block, loop_count, visited_blocking)
    if can_move_result == "yes":
        return next_move
    elif can_move_result == "end":
        return [0, 0]
    elif next_move[0] == 0 and next_move[1] == 1:
        return get_next_move(lines, y, x, [1, 0], y_block, x_block, loop_count, visited_blocking)
    elif next_move[0] == 1 and next_move[1] == 0:
        return get_next_move(lines, y, x, [0, -1], y_block, x_block, loop_count, visited_blocking)
    elif next_move[0] == 0 and next_move[1] == -1:
        return get_next_move(lines, y, x, [-1, 0], y_block, x_block, loop_count, visited_blocking)
    elif next_move[0] == -1 and next_move[1] == 0:
        return get_next_move(lines, y, x, [0, 1], y_block, x_block, loop_count, visited_blocking)
    else:
        return [0, 0]

def create_position_key(position):
    pos = str(position[0]) + "," + str(position[1])
    return pos

def part_one(s):
    rules_lines = [[char for char in x] for x in s.splitlines()]
    guard_y, guard_x, next_position = get_guard_position_and_first_move(rules_lines)

    visited = set()
    ongoing = True
    while ongoing:
        visited.add(create_position_key([guard_y, guard_x]))
        next_move = get_next_move(rules_lines, guard_y, guard_x, next_position, -1, -1, 0, {})
        if next_move == [0, 0]:
            ongoing = False
        else:
            guard_y += next_move[0]
            guard_x += next_move[1]
            next_position = next_move

    return len(visited)

execute_and_elapsed_time(lambda: print(part_one(test)), "part 1 test")
execute_and_elapsed_time(lambda: print(part_one(real)), "part 1 real")

# 6560 too high
# 6561 too high


    
    

def part_two(s):
    rules_lines = [[char for char in x] for x in s.splitlines()]
    guard_y, guard_x, next_position = get_guard_position_and_first_move(rules_lines)
    init_guard_y = guard_y
    init_guard_x = guard_x
    init_symbol = rules_lines[guard_y][guard_x]
    init_next_position = next_position

    blocking_count = 0
    for y in range(len(rules_lines)):
        for x in range(len(rules_lines[y])): 
            if rules_lines[y][x] != "#" and rules_lines[y][x] != ">" and rules_lines[y][x] != "v" and rules_lines[y][x] != "^" and rules_lines[y][x] != "<":

                visited_blocking = {}
                guard_x = init_guard_x
                guard_y = init_guard_y
                next_position = init_next_position
                rules_lines[y][x] = "#"

                loop_count = [0]
                ongoing = True
                while ongoing and loop_count[0] < 2:
                    next_move = get_next_move(rules_lines, guard_y, guard_x, next_position, y, x, loop_count, visited_blocking)
                    if next_move == [0, 0]:
                        ongoing = False
                    else:
                        guard_y += next_move[0]
                        guard_x += next_move[1]
                        next_position = next_move
                if ongoing and loop_count[0] == 2:
                    blocking_count += 1
                rules_lines[y][x] = init_symbol
    
    return blocking_count       

execute_and_elapsed_time(lambda: print(part_two(test)), "part 2 test")
execute_and_elapsed_time(lambda: print(part_two(real)), "part 2 real")

