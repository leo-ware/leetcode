"""
https://leetcode.com/problems/longest-valid-parentheses/

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
"""

def count(s):
    s = s.replace("()", "*")
    for i in range(1, len(s)):
        s = s.replace(f"(" + i * "*" + ")", (i + 1) * "*")
    s = s.replace(")", "(")
    s = s.split("(")
    return max(len(p) for p in s) * 2

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        return count(s)
