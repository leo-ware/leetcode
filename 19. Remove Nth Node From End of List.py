"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given the head of a linked list, remove the nth node from the end of the list and return its head.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""

def func(node, n):
    arr = []
    while node:
        arr.append(node)
        node = node.next
    
    i = len(arr) - n
    del arr[i]

    if i != 0:
        if i < len(arr):
            arr[i - 1].next = arr[i]
        else:
            arr[i - 1].next = None
    
    if arr:
        return arr[0]
