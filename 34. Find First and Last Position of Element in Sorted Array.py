"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?
"""

def thing(l, x):
    start = None
    for i in range(len(l)):
        if start is None:
            if l[i] == x:
                start = i
        elif l[i] != x:
            return start, i - 1
    
    if start is not None:
        return [start, len(l) - 1]
    return [-1, -1]

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return thing(nums, target)
