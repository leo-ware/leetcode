"""
https://leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""

class Solution:
    def __init__(self):
        self.solutions = None

    def generateParenthesis(self, n: int):
        self.solutions = []
        self.backtrack("", 0, 0, n)
        return self.solutions

    def backtrack(self, current, opens, closes, mx):
        if opens == closes == mx:
            self.solutions.append(current)
            return
        if opens < mx:
            self.backtrack(current + "(", opens + 1, closes, mx)
        if closes < opens:
            self.backtrack(current + ")", opens, closes + 1, mx)
