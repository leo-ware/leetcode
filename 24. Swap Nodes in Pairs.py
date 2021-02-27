"""
https://leetcode.com/problems/swap-nodes-in-pairs/

Given a linked list, swap every two adjacent nodes and return its head.
"""
def swap(head):
    if head is None or head.next is None:
        return None
    head.val, head.next.val = head.next.val, head.val
    swap(head.next.next)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        swap(head)
        return head
