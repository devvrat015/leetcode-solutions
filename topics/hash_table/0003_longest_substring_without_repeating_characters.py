"""
Problem    : 0003. Longest Substring Without Repeating Characters
Link       : https://leetcode.com/problems/longest-substring-without-repeating-characters/
Difficulty : Medium
Tags       : Hash Table, String, Sliding Window
Runtime    : 218 ms (beats 33.49%)
Memory     : 19.95 MB (beats 29.59%)
"""


class Solution:
    def lengthOfLongestSubstring(self, s:
    str) -> int:
        left = 0
        max_length = 0
        seen = set()
