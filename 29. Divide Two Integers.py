"""
https://leetcode.com/problems/divide-two-integers/

Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Note:

Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For this problem, assume that your function returns 231 − 1 when the division result overflows.
"""

from math import floor
from decimal import Decimal, getcontext
getcontext().prec = 300
e = Decimal("2.718281828459045235360287471352662497757247093699959574966967627724076630353547594571382178525166427427466391932003059921817413596629043572900334295260595630738132328627943490763233829880753195251019011573834187930702154089149934884167509244761460668082264800168477411853742345442437107539077744992069")

def divide(a, b):
    parity = ((a >= 0) == (b >= 0)) * 2 - 1
    a, b = Decimal(abs(a)), Decimal(abs(b))
    q = parity * floor(e**Decimal(a.ln() - b.ln()))
    
    if q < -2**31:
        return -2**31
    elif q > 2**31-1:
        print('hi')
        return 2**31-1
    else:
        return q

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        return divide(dividend, divisor)
