"""
https://leetcode.com/problems/trapping-rain-water/

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
"""

class Solution:
    def trap(self, heights: List[int]) -> int:
        biggest_left = []
        best = 0
        for h in heights:
            biggest_left.append(best)
            best = max(h, best)

        biggest_right = []
        best = 0
        for h in reversed(heights):
            biggest_right.append(best)
            best = max(h, best)
        biggest_right = list(reversed(biggest_right))

        water = []
        for i, h in enumerate(heights):
            water.append(max(0, min(biggest_left[i], biggest_right[i]) - h))

        return sum(water)
