"""
Problem    : 0283. Move Zeroes
Link       : https://leetcode.com/problems/move-zeroes/
Difficulty : Easy
Tags       : Array, Two Pointers
Runtime    : 0 ms (beats 17.48%)
Memory     : 20.54 MB (beats 25.81%)
"""

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        i = 0

        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
