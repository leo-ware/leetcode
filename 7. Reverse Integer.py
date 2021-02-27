"""
https://leetcode.com/problems/reverse-integer/

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""

def thing(num):
    sign = 1 if num >= 0 else -1
    num = sign*int("".join(list(reversed(str(abs(num))))))
    if not -2**31 <= num <= 2**31 - 1:
        return 0
    else:
        return num

class Solution:
    def reverse(self, i):
        return thing(i)
