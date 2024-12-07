import os
import string
from collections import defaultdict
import functools
import sys
import copy
import re
import math

#sys.setrecursionlimit(1000000)

# TEST
with open(r"input.txt") as f:
    test = f.read().strip()
    #print(s)

# REAL
with open(r"input-pt-2.txt") as f:
    real = f.read().strip()
    #print(s)

def get_middle_pages(indexes_array, orders_lines):
    result = []
    for i in indexes_array:
        line = orders_lines[i]
        middle_page = line[math.floor(len(line)/2)]
        result.append(int(middle_page))
    return result

def is_valid_order_line(rules_lines, orders_line):
    is_valid = True
    for rules in rules_lines:
        try:
            if orders_line.index(rules[0]) > orders_line.index(rules[1]):
                is_valid = False
                break
        except ValueError:
            pass  # do nothing!

    return is_valid

def get_valid_orders_indexes(rules_lines, orders_lines):
    result = []
    for i in range(len(orders_lines)):
        if is_valid_order_line(rules_lines, orders_lines[i]):
            result.append(i)
    return result

        

def part_one(s):
    rules, orders = s.split("\n\n")
    rules_lines = [x.split("|") for x in rules.splitlines()]
    orders_lines = [x.split(",") for x in orders.splitlines()]

    valid_orders_indexes = get_valid_orders_indexes(rules_lines, orders_lines)
    valid_pages = get_middle_pages(valid_orders_indexes, orders_lines)
    
    return sum(valid_pages)


print(part_one(test))
print(part_one(real))


def is_invalid_order_line(rules_lines, orders_line):
    is_invalid = False
    for rules in rules_lines:
        try:
            if orders_line.index(rules[0]) > orders_line.index(rules[1]):
                is_invalid = True
                break
        except ValueError:
            pass  # do nothing!

    return is_invalid

def rotate(order_line, page, second_page):
    try:
        new_index = order_line.index(second_page) + 1
    except ValueError:
        return order_line
        pass  # do nothing!
    order_line.remove(page)
    order_line.insert(new_index, page)

def validate_order_line(rules_lines, orders_line):
    is_invalid_line = True
    while is_invalid_line:
        all_valid = True
        for rules in rules_lines:
            try:
                if orders_line.index(rules[0]) > orders_line.index(rules[1]):
                    all_valid = False
                    rotate(orders_line, rules[1], rules[0])
            except ValueError:
                pass  # do nothing!

        if all_valid:
            is_invalid_line = False
            
    return orders_line

def get_invalid_orders_indexes(rules_lines, orders_lines):
    result = []
    for i in range(len(orders_lines)):
        if is_invalid_order_line(rules_lines, orders_lines[i]):
            result.append(i)
            validate_order_line(rules_lines, orders_lines[i])
    return result

def part_two(s):
    rules, orders = s.split("\n\n")
    rules_lines = [x.split("|") for x in rules.splitlines()]
    orders_lines = [x.split(",") for x in orders.splitlines()]

    invalid_orders_indexes = get_invalid_orders_indexes(rules_lines, orders_lines)
    invalid_pages = get_middle_pages(invalid_orders_indexes, orders_lines)
                
    return sum(invalid_pages)


print(part_two(test))
print(part_two(real))
