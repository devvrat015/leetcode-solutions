"""
Problem    : 0128. Longest Consecutive Sequence
Link       : https://leetcode.com/problems/longest-consecutive-sequence/
Difficulty : Medium
Tags       : Array, Hash Table, Union-Find
Runtime    : 0 ms (beats 53.54%)
Memory     : 36.6 MB (beats 67.56%)
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

        # Sorting + linear scan → O(n log n)
        # nums.sort()
        # prev = nums[0]
        # counter = 1

        # for i in range(1, len(nums)):

        #     if nums[i] == prev + 1:
        #         prev = nums[i]
        #         counter +=1

        # return counter
