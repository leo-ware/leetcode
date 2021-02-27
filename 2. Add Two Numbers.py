"""
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def get_str(node):
    return (get_str(node.next) if node.next else "") + str(node.val)

def write_node(string):
    return ListNode(val=int(string[-1]), next=write_node(string[:-1]) if len(string) > 1 else None)

def add_nodes(n1, n2):
    return write_node(str(int(get_str(n1)) + int(get_str(n2))))

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return add_nodes(l1, l2)
