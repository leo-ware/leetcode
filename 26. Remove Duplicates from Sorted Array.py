"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

"""

def rm(l):
    kills = 0
    last = None
    
    for i, x in enumerate(l):
        if x == last:
            kills += 1
        else:
            l[i - kills] = x
        last = x
    
    if kills:
        l = l[:-kills]
        
    return len(l)


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        return rm(nums)
