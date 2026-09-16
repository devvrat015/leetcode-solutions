"""
Problem    : 0003. Longest Substring Without Repeating Characters
Link       : https://leetcode.com/problems/longest-substring-without-repeating-characters/
Difficulty : Medium
Tags       : Hash Table, String, Sliding Window
Runtime    : 2 ms (beats 21.96%)
Memory     : 19.9 MB (beats 60.24%)
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
