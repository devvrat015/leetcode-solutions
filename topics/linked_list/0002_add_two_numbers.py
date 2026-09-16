"""
Problem    : 0002. Add Two Numbers
Link       : https://leetcode.com/problems/add-two-numbers/
Difficulty : Medium
Tags       : Linked List, Math, Recursion
Runtime    : 0 ms (beats 0.0%)
Memory     : 0.0 MB (beats 0.0%)
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return ([i, j])
