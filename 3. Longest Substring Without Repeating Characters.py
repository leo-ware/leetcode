"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best_score = 0
        for i in range(len(s)):
            substring = set()
            for j in range(i, len(s)):
                if j != i and s[j] in substring:
                    break
                else:
                    substring.add(s[j])
                    best_score = max(j - i + 1, best_score)
            
        return best_score
