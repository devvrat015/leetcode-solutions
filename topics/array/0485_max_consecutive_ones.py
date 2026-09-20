"""
Problem    : 0485. Max Consecutive Ones
Link       : https://leetcode.com/problems/max-consecutive-ones/
Difficulty : Easy
Tags       : Array
Runtime    : 0 ms (beats 30.8%)
Memory     : 21.83 MB (beats 44.22%)
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        maxi = 0 
        count = 0

        for el in nums:
            if el == 1:
                count += 1
                maxi = max(maxi, count)
            else:
                count = 0
        return maxi
