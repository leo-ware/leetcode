"""
https://leetcode.com/problems/jump-game-ii/

Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.
"""

def func(jumps):
    if len(jumps) == 1:
        return 0

    rev_jumps = reversed(jumps)
    distances = [float("inf") for _ in jumps]

    for i, jump in enumerate(rev_jumps):
        if jump >= i:
            distances[i] = 1
        else:
            options = [distances[j] for j in range(i - jump, i)]
            if options:
                distances[i] = min(options) + 1
    
    return distances[-1]
