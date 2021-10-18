"""
https://leetcode.com/problems/merge-intervals/

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the 
non-overlapping intervals that cover all the intervals in the input.
"""

import heapq as hq

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        hq.heapify(intervals)
        new = []

        while intervals:
            current = hq.heappop(intervals)
            while intervals and (intervals[0][0] <= current[1]):
                current[1] = max(hq.heappop(intervals)[1], current[1])
            new.append(current)

        return new
