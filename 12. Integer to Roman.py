"""

https://leetcode.com/problems/integer-to-roman/

Given an integer, convert it to a roman numeral.
"""

r = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I"
}

def roman(num):
    thing = []
    while num > 0:
        for value, symbol in r.items():
            if num >= value:
                num -= value
                thing.append(symbol)
                break
    return "".join(thing)



class Solution:
    def intToRoman(self, num: int) -> str:
        return roman(num)
