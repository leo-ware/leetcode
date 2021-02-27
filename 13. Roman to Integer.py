"""
https://leetcode.com/problems/roman-to-integer/

Given a roman numeral, convert it to an integer.
"""

r = {
    "M": 1000,
    "D": 500,
    "C": 100,
    "L": 50,
    "X": 10,
    "V": 5,
    "I": 1
}

def roman(s):
    if not s:
        return 0
    pivot = max(list(range(len(s))), key=lambda i: r[s[i]])
    
    value = r[s[pivot]] + roman(s[pivot + 1:])
    if pivot != 0:
        value -= roman(s[:pivot])
    
    return value


class Solution:
    def romanToInt(self, s: str) -> int:
        return roman(s)
