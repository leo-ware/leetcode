"""
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""

pairs = {
    ")": "(",
    "]": "[",
    "}": "{"
}

opens = set(pairs.values())
closes = set(pairs.keys())

def valid(s):
    seq = []
    for c in s:
        if c in opens:
            seq.append(c)
        elif c in closes:
            if not seq or seq.pop() != pairs[c]:
                return False
    return not seq

class Solution:
    def isValid(self, s: str) -> bool:
        return valid(s)
