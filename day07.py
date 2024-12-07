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
with open(r"input-bis.txt") as f:
    test = f.read().strip()
    #print(s)

# REAL
with open(r"input-bis-pt-2.txt") as f:
    real = f.read().strip()
    #print(s)


def execute_and_elapsed_time(fn, text):
    tic = time.time()
    fn()
    toc = time.time()
    elapsed_time = toc - tic
    print(f"Elapsed time {text}: {elapsed_time:.2f} seconds")


def part_one(s):
    equations = [[
        int(x.split(':')[0]),
        list(map(int,
                 x.split(':')[1].split()))
    ] for x in s.strip().splitlines()]

    nb_valid = 0

    operations = ["*", "+"]
    nb_ops = len(operations)
    for eq in equations:
        is_valid = False
        n = len(eq[1]) - 1
        for j in range(nb_ops**n):
            factors = eq[1].copy()
            factors.reverse()
            current_combination = [
                '*' if bit == '0' else '+' for bit in bin(j)[2:].zfill(n)
            ]
            
            result = 0
            first = True
            while len(current_combination) > 0:
                op = current_combination.pop()
                fac1 = factors.pop()
                fac2 = factors.pop() if first else 0
                if op == '*':
                    if first:
                        
                       result += fac1 * fac2
                    else:
                       result = fac1 * result
                else:
                    if first:
                       result += fac1 + fac2
                    else:
                       result = fac1 + result
                first = False

            if result == eq[0]:
                is_valid = True
                break

        if is_valid:
            nb_valid += eq[0]

    return nb_valid


execute_and_elapsed_time(lambda: print(part_one(test)), "part 1 test")
execute_and_elapsed_time(lambda: print(part_one(real)), "part 1 real")
#2976575 too low


def part_two(s):
    equations = [[
        int(x.split(':')[0]),
        list(map(int,
                 x.split(':')[1].split()))
    ] for x in s.strip().splitlines()]

    nb_valid = 0

    operations = ['*', '+', '||']
    nb_ops = len(operations)
    for eq in equations:
        is_valid = False
        n = len(eq[1]) - 1
        for j in range(nb_ops**n):
            factors = eq[1].copy()
            factors.reverse()
            current_combination = []
            tmp = j
            for _ in range(n):
                current_combination.append(operations[tmp % nb_ops])
                tmp //= nb_ops
            current_combination.reverse()

            result = 0
            first = True
            while len(current_combination) > 0:
                op = current_combination.pop()
                fac1 = factors.pop()
                fac2 = factors.pop() if first else 0
                if op == '*':
                    if first:
                       result += fac1 * fac2
                    else:
                       result = result * fac1
                elif op == '+':
                    if first:
                       result += fac1 + fac2
                    else:
                       result = result + fac1
                else:
                    if first:
                       result = int(str(fac1) + str(fac2))
                    else:
                       result = int(str(result) + str(fac1))
                first = False

            if result == eq[0]:
                is_valid = True
                break

        if is_valid:
            nb_valid += eq[0]

    return nb_valid


execute_and_elapsed_time(lambda: print(part_two(test)), "part 2 test")
execute_and_elapsed_time(lambda: print(part_two(real)), "part 2 real")

