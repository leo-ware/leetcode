"""
https://leetcode.com/problems/valid-sudoku/

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""

from itertools import product

def row_valid(r):
    chars = set()
    for char in r:
        if char == '.':
            continue
        elif char in chars:
            return False
        chars.add(char)
    return True

def col(j, s):
    return [s[i][j] for i in range(9)]

def box(i, j, s):
    b = []
    for _i in range(3):
        for _j in range(3):
            b.append(s[_i + i][_j + j])
    return b

def chars_valid(s):
    ints = set(str(i) for i in range(1, 10))
    ints.add(".")
    for row in s:
        for char in row:
            if char not in ints:
                print('found', char)
                return False
    return True

def valid(s):
    if not chars_valid(s):
        return False
    if not all(row_valid(row) for row in s):
        return False
    if not all(row_valid(col(i, s)) for i in range(9)):
        return False
    if not all(row_valid(box(i, j, s)) for i, j in product([0, 3, 6], [0, 3, 6])):
        return False
    return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return valid(board)
      
