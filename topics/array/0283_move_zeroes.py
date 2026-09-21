"""
Problem    : 0283. Move Zeroes
Link       : https://leetcode.com/problems/move-zeroes/
Difficulty : Easy
Tags       : Array, Two Pointers
Runtime    : 0 ms (beats 22.73%)
Memory     : 20.4 MB (beats 90.2%)
"""

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        i = 0
        j = 1
        temp = 0
        while j < len(nums):
            if nums[i] != 0:
                i+=1
            if nums[i] != nums[j]:
                temp =  nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i += 1
            j+=1
        return nums
