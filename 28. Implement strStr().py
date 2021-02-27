"""
https://leetcode.com/problems/implement-strstr/

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

"""

def first(n, h):
    if n == "":
        return 0
    
    for i in range(len(h) - len(n) + 1):
        if n == h[i:i+len(n)]:
            return i
    
    return -1

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return first(needle, haystack)
