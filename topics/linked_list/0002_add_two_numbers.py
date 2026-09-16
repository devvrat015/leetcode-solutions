"""
Problem    : 0002. Add Two Numbers
Link       : https://leetcode.com/problems/add-two-numbers/
Difficulty : Medium
Tags       : Linked List, Math, Recursion
Runtime    : 0 ms (beats 7.66%)
Memory     : 19.26 MB (beats 79.04%)
"""


        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry

            carry = total // 10
            digit = total % 10

            current.next = ListNode(digit)
            current = current.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next
