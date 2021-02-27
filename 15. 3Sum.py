"""
https://leetcode.com/problems/3sum/

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.
"""

def sum3(l):
    if len(l) < 3:
        return []
    
    l.sort()
    trips = set()
    
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
            s = sum([x, y, z])
            
            # adjust based on results
            if s == 0:
                trips.add(tuple(sorted([x, y, z])))
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
    return [list(trip) for trip in trips]

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return sum3(nums)
