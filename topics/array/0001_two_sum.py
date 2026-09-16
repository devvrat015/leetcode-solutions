"""
Problem    : 0001. Two Sum
Link       : https://leetcode.com/problems/two-sum/
Difficulty : Easy
Tags       : Array, Hash Table
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
