"""
https://leetcode.com/problems/count-and-say/

The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of groups so that each group is a contiguous section all of the same character. Then for each group, say the number of characters, then say the character. To convert the saying into a digit string, replace the counts with a number and concatenate every saying.
"""

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
    
        seqs = []
        prev = object()
        for digit in self.countAndSay(n - 1):
            if digit == prev:
                seqs[-2] += 1
            else:
                prev = digit
                seqs.append(1)
                seqs.append(digit)

        return "".join(str(x) for x in seqs)
