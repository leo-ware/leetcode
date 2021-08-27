
"""
https://leetcode.com/problems/4sum/submissions/

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.
"""

from itertools import combinations, product
from collections import defaultdict

def remove_over_four(vals):
    counts = defaultdict(lambda: 0)
    new = []
    for val in vals:
        counts[val] += 1
        if counts[val] <= 4:
            new.append(val)
    return new

def func(vals, target):
    
    # we can't ever use more than four of any one number
    # removing these is O(n) but if there are lots of duplicates 
    # it reduces the size of the input to the expensive O(n^2) part of the algorithm
    vals = remove_over_four(vals)

    combo_add = lambda combo: sum(vals[i] for i in combo)

    pairs = defaultdict(list)
    for combo in combinations(range(len(vals)), 2):
        pairs[combo_add(combo)].append(combo)
    
    wins = set()
    for key in list(pairs.keys()):
        for win in product(pairs[key], pairs[target - key]):
            win = frozenset(win[0] + win[1])
            if len(win) == 4:
                wins.add(win)

    unique_wins = frozenset(tuple(sorted(vals[i] for i in win)) for win in wins)

    return [[i for i in combo] for combo in unique_wins]
