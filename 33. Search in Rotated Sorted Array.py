"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
"""

def rot_bin_search(l, x):
    if not l:
        return -1
    
    if l[0] > x: # right of pivot
        large = lambda i: not (l[i] > l[-1] or l[i] < x)
    else: # left of pivot
        large = lambda i: l[i] < l[0] or l[i] > x
    
    upper, lower = len(l), -1
    for _ in range(1000):
        if upper - lower <= 1:
            return -1
        
        guess = (upper - lower) // 2 + lower
        if l[guess] == x:
            return guess
        elif large(guess):
            upper = guess
        else:
            lower = guess
    
    raise Error("Something went wrong")


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return rot_bin_search(nums, target)
      
