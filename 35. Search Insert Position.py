"""
https://leetcode.com/problems/search-insert-position/

Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
"""

def foo(l, i):
    lower = -1
    upper = len(l)
    
    for _ in range(1000): # if n > 1000 someone else messed up
      
        # not found
        if upper - lower <= 1:
            return upper
        
        # binary search
        guess = lower + (upper - lower) // 2
        if l[guess] == i:
            return guess
        elif l[guess] < i:
            lower = guess
        elif l[guess] > i:
            upper = guess
            
    raise ValueError("something went wrong")


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return foo(nums, target)
