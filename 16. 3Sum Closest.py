"""
https://leetcode.com/problems/3sum-closest/

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.
"""

def sum3(l, target):
    if len(l) < 3:
        return []
    
    l.sort()
    best = None
    best_score = float('inf')
    
    for x_i, x in enumerate(l):
        
        y_i, z_i = 0, len(l) - 1
        
        # if pointers clash, increment
        if y_i == x_i:
            y_i += 1
        if z_i == x_i:
            z_i -= 1
        
        while y_i < z_i:
            
            # get sum
            y, z = l[y_i], l[z_i]
            s = sum([x, y, z]) - target
            
            # update if best
            if abs(s) < best_score:
                best_score = abs(s)
                best = ([x, y, z])
            
            # adjust based on results
            if s == 0:
                y_i += 1
                z_i -= 1
            elif s < 0:
                y_i += 1
            else:
                z_i -= 1
            
            # if pointers clash, increment
            if y_i == x_i:
                y_i += 1
            if z_i == x_i:
                z_i -= 1
    
    # swap for list and return
    return sum(best)

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        return sum3(nums, target)
