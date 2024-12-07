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


pattern = r"mul\(\d+,\d+\)"

def part_one(s):
    multiplications = re.findall(pattern, s)
    extract_numbers_pattern = r"\d+,\d+"
    factors = (re.findall(extract_numbers_pattern, x) for x in multiplications)
    mults = [int(x[0].split(",")[0]) * int(x[0].split(",")[1]) for x in factors]
    return sum(mults)


print(part_one(test))
print(part_one(real))


def part_two(s):
    new_s = s.replace("\n", "")
    before_dont = re.search(r"^(.*?)(?=do\(|don't\(\))", new_s)
    before_dont_text = before_dont.group(1) if before_dont else new_s

    do_dont_pairs = re.findall(r"do\(\)(.*?)don't\(\)", new_s)

    after_last_do = re.search(r"do\(\)(?!.*don't\(\))(.*)$", new_s)
    after_last_do_text = after_last_do.group(1) if after_last_do else ""

    relevant_texts = [before_dont_text] + do_dont_pairs + [after_last_do_text]

    mul_matches = []
    for text in relevant_texts:
        mul_matches.extend(re.findall(pattern, text))

    extract_numbers_pattern = r"\d+,\d+"
    factors = (re.findall(extract_numbers_pattern, x) for x in mul_matches)
    mults = [int(x[0].split(",")[0]) * int(x[0].split(",")[1]) for x in factors]
    return sum(mults)


print(part_two(test))
print(part_two(real))

# 21065545 too low
# 70151392 too low
# 81412596 not good
# 92597300 too low
# 102478141 not good
