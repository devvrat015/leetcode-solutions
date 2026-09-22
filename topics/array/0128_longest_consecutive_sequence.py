"""
Problem    : 0128. Longest Consecutive Sequence
Link       : https://leetcode.com/problems/longest-consecutive-sequence/
Difficulty : Medium
Tags       : Array, Hash Table, Union-Find
Runtime    : 0 ms (beats 62.79%)
Memory     : 36.72 MB (beats 20.51%)
"""

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # Hash Set approach → O(n) average time, O(n) space.
        s = set(nums)
        longest = 0

        for num in s:
            if num - 1 not in s:
                current = num
                count = 1

                while current + 1 in s:
                    current += 1
                    count += 1 
                longest = max(longest, count)
        return longest
