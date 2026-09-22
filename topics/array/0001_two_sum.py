"""
Problem    : 0001. Two Sum
Link       : https://leetcode.com/problems/two-sum/
Difficulty : Easy
Tags       : Array, Hash Table
Runtime    : 0 ms (beats 41.03%)
Memory     : 20.75 MB (beats 7.51%)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # two pointer approach
        nums = [(num, i) for i, num in enumerate(nums)]
        nums.sort()

        start = 0
        end = len(nums) - 1

        while start < end:
            current = nums[start][0] + nums[end][0]

            if current == target:
                return [nums[start][1], nums[end][1]]

            elif current > target:
                end -= 1

            else:
                start += 1
            

# hashmap approach
            # hm = {}

            # for i, n in enumerate(nums):
            #     diff = target - n
            #     if diff in hm:
            #         return (hm[diff], i)
            #     hm[n] = i
