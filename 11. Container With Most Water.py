"""
https://leetcode.com/problems/container-with-most-water/

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.
"""

def max_area(l, i=0, j=None):
    if j is None:
        j = len(l) - 1
    
    best = 0
    while i != j:
        best = max(best, min(l[i], l[j]) * (j - i))
        if l[i] < l[j]:
            i += 1
        else:
            j -= 1
    return best

class Solution:
    def maxArea(self, height: List[int]) -> int:
        return max_area(height)
