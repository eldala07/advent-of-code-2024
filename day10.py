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


def create_graph(positions):
    graph = {}
    for iy, line in enumerate(positions):
        for ix, x in enumerate(line):
            graph[f"{iy},{ix}"] = {"value": "-1" if x == "." else x, "neighbours": []}
            if iy - 1 >= 0:
                graph[f"{iy},{ix}"]["neighbours"].append(f"{iy-1},{ix}")
            if iy + 1 < len(positions):
                graph[f"{iy},{ix}"]["neighbours"].append(f"{iy+1},{ix}")
            if ix - 1 >= 0:
                graph[f"{iy},{ix}"]["neighbours"].append(f"{iy},{ix-1}")
            if ix + 1 < len(line):
                graph[f"{iy},{ix}"]["neighbours"].append(f"{iy},{ix+1}")
    return graph
            


def bfs(visited, graph, node, queue):
    visited.append(node)
    queue.append(node)
    acc = 0

    while queue:         
        current_node = queue.pop() 
        current_value = int(graph[current_node]["value"])
        if current_value == 9:
            acc += 1
        
        for neighbour in graph[current_node]["neighbours"]:
            neighbour_value = int(graph[neighbour]["value"])
            if neighbour not in visited and current_value == neighbour_value - 1:
                visited.append(neighbour)
                queue.append(neighbour)

    return acc 


def part_one(s):
    positions = [[char for char in x] for x in s.splitlines()]
    graph = create_graph(positions)
    acc = 0
    for iy, line in enumerate(positions):
        for ix, x in enumerate(line):
            if x == '0':
                visited = []
                queue = []
                acc += bfs(visited, graph, f"{iy},{ix}", queue)

    
    return acc

execute_and_elapsed_time(lambda: print(part_one(test)), "part 1 test")
execute_and_elapsed_time(lambda: print(part_one(real)), "part 1 real")

def bfs_p2(visited, graph, node, queue):
    visited.append(node)
    queue.append(node)
    acc = 0

    while queue:         
        current_node = queue.pop() 
        current_value = int(graph[current_node]["value"])
        if current_value == 9:
            acc += 1

        for neighbour in graph[current_node]["neighbours"]:
            neighbour_value = int(graph[neighbour]["value"])
            if current_value == neighbour_value - 1:
                visited.append(neighbour)
                queue.append(neighbour)

    return acc 

def part_two(s):
    positions = [[char for char in x] for x in s.splitlines()]
    graph = create_graph(positions)
    acc = 0
    for iy, line in enumerate(positions):
        for ix, x in enumerate(line):
            if x == '0':
                visited = []
                queue = []
                acc += bfs_p2(visited, graph, f"{iy},{ix}", queue)
    return acc

execute_and_elapsed_time(lambda: print(part_two(test)), "part 2 test")
execute_and_elapsed_time(lambda: print(part_two(real)), "part 2 real")

