"""
Problem    : 0002. Add Two Numbers
Link       : https://leetcode.com/problems/add-two-numbers/
Difficulty : Medium
Tags       : Linked List, Math, Recursion
Runtime    : 0 ms (beats 24.45%)
Memory     : 19.17 MB (beats 96.04%)
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
