"""
https://leetcode.com/problems/permutations-ii/submissions/

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
"""

from itertools import permutations

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return list(set(permutations(nums)))
