"""
https://leetcode.com/problems/rotate-image/

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
"""

# my solution faster than 99%, less memory than 86%

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # iterate over successive "rings" of the matrix
        for c in range(n//2):
            p = list(range(c, n-c))

            path = (
                [[c, i] for i in p][:-1] +                # top
                [[i, n-c-1] for i in p][:-1] +            # right
                [[n-c-1, i] for i in reversed(p)][:-1] +  # bottom
                [[i, c] for i in reversed(p)][:-1]        # left
            )

            # copy out the values from this ring at rotate
            vals = [matrix[i][j] for i, j in path]
            rot_by = len(vals)-n+2*c+1
            new_vals = vals[rot_by:] + vals[:rot_by]

            # write them back into the array
            for pos, val in zip(path, new_vals):
                matrix[pos[0]][pos[1]] = val
