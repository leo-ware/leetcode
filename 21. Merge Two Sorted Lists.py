"""
https://leetcode.com/problems/merge-two-sorted-lists/

Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def foo(l1, l2):
    def val(l):
        if l is None:
            return float('inf')
        else:
            return l.val
    if not (l1 or l2):
        return None
    
    n = None
    while l1 or l2:
        if val(l1) <= val(l2):
            nxt = l1
            l1 = l1.next
        else:
            nxt = l2
            l2 = l2.next

        if n:
            n.next = nxt
            n = n.next
        else:
            n = nxt
            top = n

    return top

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        return foo(l1, l2)
        
