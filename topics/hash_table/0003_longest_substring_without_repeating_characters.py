"""
Problem    : 0003. Longest Substring Without Repeating Characters
Link       : https://leetcode.com/problems/longest-substring-without-repeating-characters/
Difficulty : Medium
Tags       : Hash Table, String, Sliding Window
Runtime    : 186 ms (beats 67.21%)
Memory     : 20.07 MB (beats 9.61%)
"""


class Solution:
    def lengthOfLongestSubstring(self, s:
    str) -> int:
        left = 0
        max_length = 0
        seen = set()

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1


        return max_length
