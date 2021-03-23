"""
https://leetcode.com/problems/first-missing-positive/

Given an unsorted integer array nums, find the smallest missing positive integer.
"""

# the problem statement specifies the list has no more than 300 elements
# so this quick and short solution works

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        for i in range(1, 302):
            if i not in nums:
                return i
        raise ValueError("list has more than 300 elements")
