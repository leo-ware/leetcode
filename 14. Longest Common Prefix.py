"""
https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not len(strs):
            return ""
        prefix = []
        for i in range(min(len(x) for x in strs)):
            char = strs[0][i]
            if all(x[i] == char for x in strs):
                prefix.append(char)
            else:
                break
        return "".join(prefix)
