
"""
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

"""


def max_subarray(arr):
    if not arr:
        return None
    
    max_val = float("-inf")
    max_ends_here = 0

    for x in arr:
        max_ends_here += x
        max_val = max(max_val, max_ends_here)
        max_ends_here = max(max_ends_here, 0)
    
    return max_val
