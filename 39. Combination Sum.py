"""
https://leetcode.com/problems/combination-sum/

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates 
where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at 
least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
"""

# For reasons I don't understand, caching seemed to slow it down

# from functools import lru_cache
# @lru_cache
def make(t, c):
    if not c or t < 1:
        return []

    return (
        ([(t,)] if t in c else []) + # trivial combo
        [(c[0], *combo) for combo in make(t-c[0], c)] + # combos w/ c[0]
        make(t, c[1:]) # combos w/o c[0]
    )

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return [list(sol) for sol in set(make(target, tuple(sorted(candidates))))]
