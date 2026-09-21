"""
Problem    : 0026. Remove Duplicates from Sorted Array
Link       : https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Difficulty : Easy
Tags       : Array, Two Pointers
Runtime    : 0 ms (beats 12.57%)
Memory     : 20.57 MB (beats 43.63%)
"""

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        i = 0
        j = 1

        while j < len(nums):
            if nums[i] != nums[j]:
                nums[i+1] = nums[j]
                i += 1
            j+=1
        return i+1
