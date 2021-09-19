"""
https://leetcode.com/problems/unique-paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""

def unique_paths(m, n, downs=1, rights=1):
    grid = [[0 for _ in range(n)] for _ in range(m)]
    grid[-1][-1] = 1

    for n_i in reversed(range(n)):
        for m_i in reversed(range(m)):
            if m_i+1 < m:
                grid[m_i][n_i] += grid[m_i+1][n_i]
            if n_i+1 < n:
                grid[m_i][n_i] += grid[m_i][n_i+1]

    return grid[0][0]
