"""
https://leetcode.com/problems/merge-k-sorted-lists/

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def make_list(l):
    if not l:
        return None
    return ListNode(val=l[0], next=make_list(l[1:]))

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        vals = []
        for l in lists:
            while l:
                vals.append(l.val)
                l = l.next

        vals.sort()
        return make_list(vals)
