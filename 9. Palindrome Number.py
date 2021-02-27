"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.
"""

def p(num):
    return _p(str(num))
    
def _p(num):
    if not len(num):
        return True
    return num[0] == num[-1] and _p(num[1:-1])

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return p(x)
