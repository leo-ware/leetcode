"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""

chars = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}

def words(s):
    s = str(s)
    if not s:
        return ""
    elif len(s) == 1:
        return chars[s[0]]
    
    ws = []
    for word in words(s[1:]):
        for char in chars[s[0]]:
            ws.append(char + word)
    
    return ws

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        return words(digits)
