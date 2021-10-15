
"""
https://leetcode.com/problems/jump-game/

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        nearest_reach = len(nums) - 1
        for i, val in reversed(list(enumerate(nums))):
            if i + val >= nearest_reach:
                nearest_reach = i
        return nearest_reach == 0
