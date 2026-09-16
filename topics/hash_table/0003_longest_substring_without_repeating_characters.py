"""
Problem    : 0003. Longest Substring Without Repeating Characters
Link       : https://leetcode.com/problems/longest-substring-without-repeating-characters/
Difficulty : Medium
Tags       : Hash Table, String, Sliding Window
Runtime    : 187 ms (beats 66.78%)
Memory     : 19.85 MB (beats 60.24%)
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        seen = set()

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length
