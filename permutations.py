"""
https://leetcode.com/problems/permutations/submissions/

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

"""

def copy_insert(l, item, i):
    l = l.copy()
    l.insert(i, item)
    return l

def prm(l):
    if len(l) == 1:
        return [l]
    
    result = []
    for kid in prm(l[1:]):
        for i in range(len(kid) + 1):
            result.append(copy_insert(kid, l[0], i))
    
    return result


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return prm(nums)
