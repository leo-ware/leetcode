"""
https://leetcode.com/problems/next-permutation/

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.
"""

def next_p(l):
    if not l:
        return l
    
    # find reversed tail
    for i, j in zip(reversed(range(len(l))), reversed(range(-1, len(l) - 1))):
        if l[j] < l[i]:
            break
    
    # sort reversed tail
    a, b = i, len(l) - 1
    while a < b:
        l[a], l[b] = l[b], l[a]
        a += 1
        b -= 1
    
    # find next greatest and swap
    best = i - 1
    for k in range(i, len(l)):
        if l[k] > l[i - 1] and ((best == i - 1) or (l[best] > l[k])):
            best = k
    l[i - 1], l[best] = l[best], l[i - 1]
    
    return l



class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        next_p(nums)
        
