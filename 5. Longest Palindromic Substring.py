"""
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, return the longest palindromic substring in s.
"""

def func(s):
    table = [[False for _ in s] for _ in s]
    best = ""
    for l in range(1, len(s) + 1):
        for start in range(len(s) - l + 1):
            stop = start + l - 1
            if (s[start] == s[stop]) and (l <= 2 or table[start + 1][stop - 1]):
                table[start][stop] = True
                if l > len(best):
                    best = s[start:stop + 1]
    return best
