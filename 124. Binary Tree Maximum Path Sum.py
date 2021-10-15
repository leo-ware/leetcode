"""
https://leetcode.com/problems/binary-tree-maximum-path-sum/

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any path.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def max_path(node):
    if node == None:
        return (-float("inf"), -float("inf"))
    
    left_one, left_two = max_path(node.left)
    right_one, right_two = max_path(node.right)

    left_one = max(left_one, 0)
    right_one = max(right_one, 0)
    
    # best two-sided path
    my_two = max(
        left_two,
        right_two,
        left_one + right_one + node.val
    )
    
    # best one-sided path
    my_one = max(left_one, right_one) + node.val

    return my_one, my_two

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return max(max_path(root))
